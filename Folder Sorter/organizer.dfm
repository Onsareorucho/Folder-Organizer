object frmMain: TfrmMain
  Left = 0
  Top = 0
  Caption = 'Folder Sort'
  ClientHeight = 707
  ClientWidth = 522
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object btnSelectFolder: TSpeedButton
    Left = 8
    Top = 8
    Width = 89
    Height = 22
    Caption = 'Select Folder'
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Segoe UI Semibold'
    Font.Style = [fsBold]
    ParentFont = False
    OnClick = btnSelectFolderClick
  end
  object btnOrganize: TSpeedButton
    Left = 8
    Top = 672
    Width = 89
    Height = 22
    Caption = 'Organize'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clGreen
    Font.Height = -15
    Font.Name = 'Segoe UI'
    Font.Style = [fsBold]
    ParentFont = False
    OnClick = btnOrganizeClick
  end
  object Selected_Folder: TGroupBox
    Left = 9
    Top = 36
    Width = 499
    Height = 622
    Caption = 'Selected Folder'
    TabOrder = 0
    object listBoxFolder: TListBox
      Left = 2
      Top = 17
      Width = 495
      Height = 603
      Align = alClient
      ItemHeight = 15
      TabOrder = 0
    end
  end
end
