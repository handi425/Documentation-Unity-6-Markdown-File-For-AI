[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [EditorUtility](EditorUtility.html).SaveFilePanelInProject

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static string SaveFilePanelInProject(string title, string defaultName,
string extension, string message);

## Declaration

public static string SaveFilePanelInProject(string title, string defaultName,
string extension, string message, string path);

### Parameters

title | The title of the window to display.  
---|---  
defaultName | The placeholder text to display in the "Save As" text field. This is the name of file to be saved.   
extension | The file extension to use in the saved file path. For example, enter "png" to save an image in the PNG format.  
message | The text summary to display in the dialog window.  
path | The working directory for this dialog to open in. The default value is "Assets.".  
  
### Returns

**string** A string path to the saved file. If the dialog was canceled or the
save failed, it returns an empty string.

### Description

Displays the "save file" dialog in the Assets folder of the project and
returns the selected path name.

Additional resources: [SaveFilePanel](EditorUtility.SaveFilePanel.html)
function.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilitySaveFilePanelInProject.png)  
_Save File panel in project._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;  
      
    public class SaveFilePanelInProjectExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Example/Save [Texture](Texture.html) In Project")]
        static void Apply()
        {
            [Texture2D](Texture2D.html) texture = [Selection.activeObject](Selection-activeObject.html) as [Texture2D](Texture2D.html);
            if (texture == null)
            {
                [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Select [Texture](Texture.html)", "You must select a texture first!", "OK");
                return;
            }  
      
            string path = [EditorUtility.SaveFilePanelInProject](EditorUtility.SaveFilePanelInProject.html)("Save png", texture.name + "png", "png",
                "Please enter a file name to save the texture to");
            if (path.Length != 0)
            {
                byte[] pngData = texture.EncodeToPNG();
                if (pngData != null)
                {
                    [File.WriteAllBytes](Windows.File.WriteAllBytes.html)(path, pngData);  
      
                    // As we are saving to the asset folder, tell Unity to scan for modified or new assets
                    [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
                }
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

