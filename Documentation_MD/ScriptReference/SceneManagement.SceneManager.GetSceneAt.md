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

#  [SceneManager](SceneManagement.SceneManager.html).GetSceneAt

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

public static [SceneManagement.Scene](SceneManagement.Scene.html)
GetSceneAt(int index);

### Parameters

index | Index of the Scene to get. Index must be greater than or equal to 0 and less than SceneManager.sceneCount.  
---|---  
  
### Returns

**Scene** A reference to the Scene at the index specified.

### Description

Get the Scene at index in the SceneManager's list of loaded Scenes.

    
    
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.SceneManagement;  
      
    public class Example
    {
        // adds a menu item which gives a brief summary of currently open Scenes
        [[MenuItem](MenuItem.html)("SceneExample/[Scene](SceneManagement.Scene.html) Summary")]
        public static void ListSceneNames()
        {
            StringBuilder sb;  
      
            if ([SceneManager.sceneCount](SceneManagement.SceneManager-sceneCount.html) > 0)
            {
                sb = new StringBuilder();
                for (int n = 0; n < [SceneManager.sceneCount](SceneManagement.SceneManager-sceneCount.html); ++n)
                {
                    [Scene](SceneManagement.Scene.html) scene = [SceneManager.GetSceneAt](SceneManagement.SceneManager.GetSceneAt.html)(n);
                    sb.Append(scene.name);
                    sb.Append(scene.isLoaded ? " (Loaded, " : " (Not Loaded, ");
                    sb.Append(scene.isDirty ? "Dirty, " : "Clean, ");
                    sb.Append(scene.buildIndex >= 0 ? " in build)\n" : " NOT in build)\n");
                }
            }
            else
            {
                sb = new StringBuilder("No open Scenes.");
            }
            [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("[Scene](SceneManagement.Scene.html) Summary", sb.ToString(), "OK");
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

