from pyreutils import *
from dfpyre import *

# Initialize Variables
width = Var('width', 'line')
height = Var('height', 'line')
radius = Var('radius', 'line')
k = Var('k', 'line')

cell_size = Var('cell_size', 'local')
cols = Var('cols', 'local')
rows = Var('rows', 'local')
grid = Var('grid', 'local')          # Dictionary: "col,row" -> point_index
points = Var('points', 'local')      # List of Vectors (locations)
active_list = Var('active_list', 'local') # List of indices
temp_vec = Var('temp_vec', 'local')

start_x = Var('start_x', 'local')
start_y = Var('start_y', 'local')
start_pos = Var('start_pos', 'local')
g_col = Var('g_col', 'local')
g_row = Var('g_row', 'local')
grid_key = Var('grid_key', 'local')

rand_idx = Var('random_idx', 'local')
point_idx = Var('point_idx', 'local')
base_point = Var('base_point', 'local')
found_new = Var('found_new', 'local')
angle = Var('angle', 'local')
dist = Var('dist', 'local')
offset = Var('offset', 'local')
new_pos = Var('new_pos', 'local')
new_x = Var('new_x', 'local')
new_y = Var('new_y', 'local')
col = Var('col', 'local')
row = Var('row', 'local')
ok = Var('ok', 'local')
n_col = Var('n_col', 'local')
n_row = Var('n_row', 'local')
n_key = Var('n_key', 'local')
new_pos_loc = Var('new_pos_loc', 'local')
neighbor_pt_loc = Var('neighbor_pt_loc', 'local')
neighbor_idx = Var('neighbor_idx', 'local')
neighbor_pt = Var('neighbor_pt', 'local')
current_dist = Var('current_dist', 'local')
new_idx = Var('new_idx', 'local')
final_key = Var('final_key', 'local')

list_len = Var('list_len', 'local')
r2 = Var('r2', 'local')
i = Var('i', 'local')
j = Var('j', 'local')

loop_count = Var('loop_count', 'local')

MATH_SQRT_2 = 1.41421

def init_poisson_disc_sampling():
    return [
        # --- 1. Initialize Grid ---
        # cell_size = radius / sqrt(2) (~1.41421)
        SV.Divide(cell_size, [radius, MATH_SQRT_2]),

        # Initialize data structures
        SV.CreateDict(grid),
        SV.CreateList(points),
        SV.CreateList(active_list),

        # --- 2. Add First Point ---
        # Generate random starting vector
        SV.RandomNumber(start_x, 0, width, rounding_mode='Decimal number'),
        SV.RandomNumber(start_y, 0, height, rounding_mode='Decimal number'),
        SV.Vector(start_pos, start_x, 0, start_y),

        # Add to lists
        SV.AppendValue(points, start_pos),
        SV.AppendValue(active_list, 1),

        # Update Grid
        # Col/Row calculation: int(val / cell_size)
        SV.Divide(g_col, [start_x, cell_size]),
        SV.Divide(g_row, [start_y, cell_size]),
        SV.RoundNumber(g_col, round_mode='Floor'),
        SV.RoundNumber(g_row, round_mode='Floor'),
        
        # Create key "col,row" and set grid
        SV.String(grid_key, [g_col, ",", g_row]),
        SV.SetDictValue(grid, grid_key, 1),
    ]
    
def poisson_disc_sampling():
    return [
        # --- 3. Grow Points ---
        # Loop while active_list is not empty
        #
        Repeat.While(
            [active_list, 0],
            sub_action='ListSizeEquals',
            inverted=True,  
            codeblocks=[
                IfVariable.Equals(Num("%math(%var(loop_count) % 10)"), 0, codeblocks=[
                    Control.Wait(1),
                ]),
                SV.Increment(loop_count),
                CallFunction("!!! CPUWait"),
                # Get random point from active list
                SV.ListLength(list_len, active_list),
                Control.PrintDebug(['Active List Size: ', list_len]),
                SV.RandomNumber(rand_idx, 1, list_len),
                SV.GetListValue(point_idx, active_list, rand_idx),
                SV.GetListValue(base_point, points, point_idx),
                
                # Reset found_new
                SV.Set(found_new, 0),

                # Try k times
                Repeat.Multiple(k, codeblocks=[
                    CallFunction("!!! CPUWait"),

                    # Random Angle (0-360) and Distance (r to 2r)
                    SV.RandomNumber(angle, 0, 360, rounding_mode='Decimal number'),
                    SV.Multiply(r2, [radius, 2]), # 2 * radius
                    SV.RandomNumber(dist, radius, r2, rounding_mode='Decimal number'),

                    # Calculate new position using vector math (Base + Offset)
                    # Create offset vector
                    SV.Vector(offset, 0, 0, 1), # Forward vector
                    SV.RotateAroundAxis(offset, angle, axis='Y'), # Rotate Y for flat plane logic
                    
                    SV.MultiplyVector(offset, dist),
                    
                    # Calculate new position
                    SV.AddVectors(new_pos, [base_point, offset]),
                    
                    # Extract X/Y
                    SV.GetVectorComp(new_x, new_pos, component='X'),
                    SV.GetVectorComp(new_y, new_pos, component='Z'), # Using Z as Y for 2D map logic usually

                    # Check Bounds (0 <= x <= width AND 0 <= y <= height)
                    IfVariable.InRange(new_x, 0, width, codeblocks=[
                        IfVariable.InRange(new_y, 0, height, codeblocks=[
                            
                            # Check Grid Neighbors
                            SV.Divide(col, [new_x, cell_size]),
                            SV.RoundNumber(col, round_mode='Floor'),
                            
                            SV.Divide(row, [new_y, cell_size]),
                            SV.RoundNumber(row, round_mode='Floor'),
                            
                            SV.String(final_key, [col, ",", row]),
                            
                            # If grid cell is not 
                            IfVariable.DictHasKey(grid, final_key, inverted=True, codeblocks=[
                                SV.Set(ok, 1),
                                # 5x5 Neighbor Loop (-2 to 2)
                                Repeat.Range([i, -2, 2], codeblocks=[
                                    CallFunction("!!! CPUWait"),
                                    SV.Add(n_col, [col, i]),
                                    Repeat.Range([j, -2, 2], codeblocks=[
                                        CallFunction("!!! CPUWait"),
                                        SV.Add(n_row, [row, j]),
                                        
                                        # Check if neighbor has point
                                        SV.String(n_key, [n_col, ",", n_row]),
                                        
                                        IfVariable.DictHasKey(grid, n_key, codeblocks=[
                                            SV.GetDictValue(neighbor_idx, grid, n_key),
                                            SV.GetListValue(neighbor_pt, points, neighbor_idx),
                                            
                                            SV.ShiftOnVector(new_pos_loc, Loc(), new_pos),
                                            SV.ShiftOnVector(neighbor_pt_loc, Loc(), neighbor_pt),
                                            
                                            # Distance Check
                                            SV.Distance(current_dist, new_pos_loc, neighbor_pt_loc),
                                            
                                            IfVariable.LessEqual(current_dist, radius, codeblocks=[
                                                SV.Set(ok, 0),
                                                Control.StopRepeat() # Break inner loop
                                            ])
                                        ]),
                                    ]),
                                    IfVariable.Equals(ok, 0, codeblocks=[
                                        Control.StopRepeat() # Break outer neighbor loop
                                    ])
                                ]),
                                
                                # If valid, add point
                                IfVariable.Equals(ok, 1, codeblocks=[
                                    SV.AppendValue(points, new_pos),
                                    SV.ListLength(new_idx, points),
                                    SV.AppendValue(active_list, new_idx),
                                    
                                    # Update Grid
                                    SV.SetDictValue(grid, final_key, new_idx),
                                    
                                    SV.Set(found_new, 1),
                                    Control.StopRepeat() # Break k loop
                                ])
                            ]),
                            
                        ])
                    ])
                ]),
                
                # If not found after k tries, remove from active list
                IfVariable.Equals(found_new, 0, codeblocks=[
                    SV.RemoveListIndex(active_list, rand_idx)
                ])
            ]
        )
    ]

# Define the function
t = Function(
    'poisson_disc_sampling',
    [Parameter('width', ParameterType.NUMBER),
    Parameter('height', ParameterType.NUMBER),
    Parameter('radius', ParameterType.NUMBER),
    Parameter('k', ParameterType.NUMBER, optional=True, default_value=30)],
    codeblocks=[
        init_poisson_disc_sampling(),
        poisson_disc_sampling()
    ]
)

# Build and export
t.build_and_send()