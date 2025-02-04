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

#  [SceneManager](SceneManagement.SceneManager.html).CreateScene

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
CreateScene(string sceneName);

## Declaration

public static [SceneManagement.Scene](SceneManagement.Scene.html)
CreateScene(string sceneName,
[SceneManagement.CreateSceneParameters](SceneManagement.CreateSceneParameters.html)
parameters);

### Parameters

sceneName | The name of the new Scene. It cannot be empty or null, or same as the name of the existing Scenes.  
---|---  
parameters | Various parameters used to create the Scene.  
  
### Returns

**Scene** A reference to the new Scene that was created, or an invalid Scene
if creation failed.

### Description

Create an empty new Scene at runtime with the given name.

The new Scene will be opened additively into the hierarchy alongside any
existing Scenes that are currently open. The path of the new Scene will be
empty. This function is for creating Scenes at runtime. To create a Scene at
edit-time (for example, when making an editor script or tool which needs to
create Scenes), use
[EditorSceneManager.NewScene](SceneManagement.EditorSceneManager.NewScene.html).

    
    
    using UnityEngine.SceneManagement;
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Awake()
        {
            [Scene](SceneManagement.Scene.html) newScene = [SceneManager.CreateScene](SceneManagement.SceneManager.CreateScene.html)("My New [Scene](SceneManagement.Scene.html)");
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

