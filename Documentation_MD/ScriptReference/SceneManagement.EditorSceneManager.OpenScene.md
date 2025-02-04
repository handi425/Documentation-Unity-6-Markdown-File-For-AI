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

#  [EditorSceneManager](SceneManagement.EditorSceneManager.html).OpenScene

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
OpenScene(string scenePath,
[SceneManagement.OpenSceneMode](SceneManagement.OpenSceneMode.html) mode =
OpenSceneMode.Single);

### Parameters

scenePath | The path of the Scene. This should be relative to the Project folder; for example, "Assets/MyScenes/MyScene.unity".  
---|---  
mode | Allows you to select how to open the specified Scene, and whether to keep existing Scenes in the Hierarchy. See [OpenSceneMode](SceneManagement.OpenSceneMode.html) for more information about the options.  
  
### Returns

**Scene** A reference to the opened Scene.

### Description

Open a Scene in the Editor.

Use this function to open Scenes in the Hierarchy while in the Editor, for
example for making custom Editor scripts, tools, or menu items. Do not use it
for loading Scenes at run time. To load Scenes at run time, see
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html).  
  
If the function fails for any reason (for example, because of a wrong file
path), it will throw an ArgumentException.

    
    
    //Create a new folder (Right click in the Assets folder, **Create** >**Folder**) and name it “[Editor](Editor.html)” if one doesn’t already exist
    //Put this script in the folder  
      
    //This script creates a new menu (Examples) and item (Open [Scene](SceneManagement.Scene.html)). If you choose this item in the [Editor](Editor.html), the [EditorSceneManager](SceneManagement.EditorSceneManager.html) opens the [Scene](SceneManagement.Scene.html) at the given directory (In this case, the “Scene2” [Scene](SceneManagement.Scene.html) is located in the Assets folder). This allows you to open Scenes while still working with the [Editor](Editor.html).  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SceneManagement;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Create a new drop-down menu in [Editor](Editor.html) named "Examples" and a new option called "Open [Scene](SceneManagement.Scene.html)"
        [[MenuItem](MenuItem.html)("Examples/Open [Scene](SceneManagement.Scene.html)")]
        static void OpenScene()
        {
            //Open the [Scene](SceneManagement.Scene.html) in the [Editor](Editor.html) (do not enter Play [Mode](SceneManagement.PrefabStage.Mode.html))
            [EditorSceneManager.OpenScene](SceneManagement.EditorSceneManager.OpenScene.html)("Assets/Scene2.unity");
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

