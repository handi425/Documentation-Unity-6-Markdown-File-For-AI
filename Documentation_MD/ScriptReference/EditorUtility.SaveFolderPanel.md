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

#  [EditorUtility](EditorUtility.html).SaveFolderPanel

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

public static string SaveFolderPanel(string title, string folder, string
defaultName);

### Description

Displays the "save folder" dialog and returns the selected path name.

Additional resources: [SaveFilePanel](EditorUtility.SaveFilePanel.html),
[OpenFilePanel](EditorUtility.OpenFilePanel.html) functions.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilitySaveFolderPanel.png)  
_Save Folder Panel._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;  
      
    public class SaveFolderPanelExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Example/Save Textures To [Folder](WSA.Folder.html)")]
        static void Apply()
        {
            Object[] textures = [Selection.GetFiltered](Selection.GetFiltered.html)(typeof([Texture2D](Texture2D.html)), [SelectionMode.Unfiltered](SelectionMode.Unfiltered.html));
            if (textures.Length == 0)
            {
                [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Select Textures", "You must select at least one texture first!", "OK");
                return;
            }  
      
            string path = [EditorUtility.SaveFolderPanel](EditorUtility.SaveFolderPanel.html)("Save textures to folder", "", "");
            if (path.Length != 0)
            {
                foreach ([Texture2D](Texture2D.html) texture in textures)
                {
                    [Texture2D](Texture2D.html) processedTex = texture;  
      
                    byte[] pngData = processedTex.EncodeToPNG();
                    if (pngData != null)
                        [File.WriteAllBytes](Windows.File.WriteAllBytes.html)(path + "/" + texture.name + ".png", pngData);
                    else
                        [Debug.Log](Debug.Log.html)("Could not convert " + texture.name + " to png. Skipping saving texture.");
                }  
      
                // Just in case we are saving to the asset folder, tell Unity to scan for modified or new assets
                [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
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

