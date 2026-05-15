import sys
import vtk
import numpy as np

vol_filename = sys.argv[1]

volreader = vtk.vtkXMLImageDataReader()
volreader.SetFileName(vol_filename)
volreader.Update()

vol_data = volreader.GetOutput()
point_data = vol_data.GetPointData()

# Автоматичне визначення імені масиву, якщо 'Scalars_' відсутнє
sf_name = 'Scalars_'
if not point_data.HasArray(sf_name) and point_data.GetNumberOfArrays() > 0:
    sf_name = point_data.GetArrayName(0)
    print(f"[*] Автоматично знайдено масив даних: '{sf_name}'")

point_data.SetActiveScalars(sf_name)
data_range = point_data.GetScalars().GetRange()

np.save(sys.argv[2], np.array([data_range[0], data_range[1]]))

print('range:', data_range[0], data_range[1])