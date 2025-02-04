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

#  [SceneManager](SceneManagement.SceneManager.html).UnloadSceneAsync

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

public static [AsyncOperation](AsyncOperation.html) UnloadSceneAsync(int
sceneBuildIndex);

## Declaration

public static [AsyncOperation](AsyncOperation.html) UnloadSceneAsync(string
sceneName);

## Declaration

public static [AsyncOperation](AsyncOperation.html)
UnloadSceneAsync([SceneManagement.Scene](SceneManagement.Scene.html) scene);

## Declaration

public static [AsyncOperation](AsyncOperation.html) UnloadSceneAsync(int
sceneBuildIndex,
[SceneManagement.UnloadSceneOptions](SceneManagement.UnloadSceneOptions.html)
options);

## Declaration

public static [AsyncOperation](AsyncOperation.html) UnloadSceneAsync(string
sceneName,
[SceneManagement.UnloadSceneOptions](SceneManagement.UnloadSceneOptions.html)
options);

## Declaration

public static [AsyncOperation](AsyncOperation.html)
UnloadSceneAsync([SceneManagement.Scene](SceneManagement.Scene.html) scene,
[SceneManagement.UnloadSceneOptions](SceneManagement.UnloadSceneOptions.html)
options);

### Parameters

sceneBuildIndex | Index of the Scene in BuildSettings.  
---|---  
sceneName | Name or path of the Scene to unload.  
scene | Scene to unload.  
options | Scene unloading options.  
  
### Returns

**AsyncOperation** Use the [AsyncOperation](AsyncOperation.html) to determine
if the operation has completed.

### Description

Destroys all GameObjects associated with the given Scene and removes the Scene
from the SceneManager.

The given Scene name can either be the full Scene path, the path shown in the
Build Settings window or just the Scene name. If only the Scene name is given
this will unload the first Scene in the list that matches. If you have
multiple Scenes with same name but different paths, you should use the full
Scene path. Examples of supported formats:  
`"Scene1"`  
`"Scene2"`  
`"Scenes/Scene3"`  
`"Scenes/Others/Scene3"`  
`"Assets/scenes/others/scene3.unity"`  
  
**Note:** This is case-insensitive and due to it being async there are no
guarantees about completion time.  
**Note:** Assets are currently not unloaded. In order to free up asset memory
call [Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html).  
**Note:** It is not possible to
[UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html) if
there are no scenes to load. For example, a project that has a single scene
cannot use this static member.

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

