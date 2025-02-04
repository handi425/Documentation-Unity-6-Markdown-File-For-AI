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

#  [EditorUtility](EditorUtility.html).SaveFilePanel

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

public static string SaveFilePanel(string title, string directory, string
defaultName, string extension);

### Parameters

title | The title of the window to display.  
---|---  
directory | The working directory that this dialog opens on.  
defaultName | The placeholder text to display in the "Save As" text field. This is the name of file to be saved.   
extension | The file extension to use in the saved file path. For example, enter "png" to save an image in the PNG format.  
  
### Returns

**string** A string path to the saved file if the dialog was canceled or the
save failed, it returns an empty string.

### Description

Displays the "save file" dialog and returns the selected path name.

This function displays a dialog that prompts the user for a path to save an
asset to. It does not create the file or parent directories. You are
responsible for creating and writing to the file at the returned path
location. **Note:** The dialog has a Save button and a Cancel button. If you
click the Cancel button, the window closes without saving.  
  
Additional resources: [OpenFilePanel](EditorUtility.OpenFilePanel.html)
function.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilitySaveFilePanel.png)  
_Save File Panel._

    
    
    // Opens a file selection dialog for a PNG file and saves a selected texture to the file.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.IO;  
      
    public class EditorUtilitySaveFilePanel : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Save [Texture](Texture.html) to file")]
        static void Apply()
        {
            [Texture2D](Texture2D.html) texture = [Selection.activeObject](Selection-activeObject.html) as [Texture2D](Texture2D.html);
            if (texture == null)
            {
                [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)(
                    "Select [Texture](Texture.html)",
                    "You Must Select a [Texture](Texture.html) first!",
                    "OK");
                return;
            }  
      
            var path = [EditorUtility.SaveFilePanel](EditorUtility.SaveFilePanel.html)(
                "Save texture as PNG",
                "",
                texture.name + ".png",
                "png");  
      
            if (path.Length != 0)
            {
                var pngData = texture.EncodeToPNG();
                if (pngData != null)
                    [File.WriteAllBytes](Windows.File.WriteAllBytes.html)(path, pngData);
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

