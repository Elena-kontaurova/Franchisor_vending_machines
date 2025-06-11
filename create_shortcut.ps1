# ���� (�������� �� ����!)
$exePath = "C:\Users\Home\Desktop\franchisor_vending_machines"
$iconPath = "C:\Users\Home\Desktop\franchisor_vending_machines\Frame-30.ico"
$shortcutPath = [Environment]::GetFolderPath("Desktop") + "\vendingMachines.lnk"

# �������� ������
$WScriptShell = New-Object -ComObject WScript.Shell
$shortcut = $WScriptShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $exePath
$shortcut.IconLocation = $iconPath
$shortcut.Save()