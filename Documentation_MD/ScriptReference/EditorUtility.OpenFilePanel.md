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

#  [EditorUtility](EditorUtility.html).OpenFilePanel

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

public static string OpenFilePanel(string title, string directory, string
extension);

### Parameters

title | The text to display in the toolbar of the dialog window.   
---|---  
directory | The default file directory that this dialog opens. This parameter is relative to the project directory. For example, "Assets" displays the Assets directory when this dialog opens.  
extension | The file extensions to filter in this dialog. Do not precede file extension names with a period. Enter an empty string to include all file types. Separate multiple file extensions with a comma.  
  
### Description

Displays the "open file" dialog and returns the selected path name.

Additional resources: [SaveFilePanel](EditorUtility.SaveFilePanel.html)
function.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityOpenFilePanel.png)  
_Open File Panel._

    
    
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class OpenFilePanelExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Example/Overwrite [Texture](Texture.html)")]
        static void Apply()
        {
            [Texture2D](Texture2D.html) texture = [Selection.activeObject](Selection-activeObject.html) as [Texture2D](Texture2D.html);
            if (texture == null)
            {
                [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Select [Texture](Texture.html)", "You must select a texture first!", "OK");
                return;
            }  
      
            string path = [EditorUtility.OpenFilePanel](EditorUtility.OpenFilePanel.html)("Overwrite with png", "", "png");
            if (path.Length != 0)
            {
                var fileContent = [File.ReadAllBytes](Windows.File.ReadAllBytes.html)(path);
                texture.LoadImage(fileContent);
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

