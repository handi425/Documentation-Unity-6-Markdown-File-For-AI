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

# SceneManager

class in UnityEngine.SceneManagement

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Scene management at run-time.

### Static Properties

[loadedSceneCount](SceneManagement.SceneManager-loadedSceneCount.html)| The
number of loaded Scenes.  
---|---  
[sceneCount](SceneManagement.SceneManager-sceneCount.html)| The current number
of Scenes.  
[sceneCountInBuildSettings](SceneManagement.SceneManager-
sceneCountInBuildSettings.html)| Number of Scenes in Build Settings.  
  
### Static Methods

[CreateScene](SceneManagement.SceneManager.CreateScene.html)| Create an empty
new Scene at runtime with the given name.  
---|---  
[GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)| Gets the
currently active Scene.  
[GetSceneAt](SceneManagement.SceneManager.GetSceneAt.html)| Get the Scene at
index in the SceneManager's list of loaded Scenes.  
[GetSceneByBuildIndex](SceneManagement.SceneManager.GetSceneByBuildIndex.html)|
Get a Scene struct from a build index.  
[GetSceneByName](SceneManagement.SceneManager.GetSceneByName.html)| Searches
through the Scenes loaded for a Scene with the given name.  
[GetSceneByPath](SceneManagement.SceneManager.GetSceneByPath.html)| Searches
all Scenes loaded for a Scene that has the given asset path.  
[LoadScene](SceneManagement.SceneManager.LoadScene.html)| Loads the Scene by
its name or index in Build Settings.  
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)| Loads the
Scene asynchronously in the background.  
[MergeScenes](SceneManagement.SceneManager.MergeScenes.html)| This will merge
the source Scene into the destinationScene.  
[MoveGameObjectsToScene](SceneManagement.SceneManager.MoveGameObjectsToScene.html)|
Move multiple GameObjects, represented by a NativeArray of instance IDs, from
their current Scene to a new Scene.  
[MoveGameObjectToScene](SceneManagement.SceneManager.MoveGameObjectToScene.html)|
Move a GameObject from its current Scene to a new Scene.  
[SetActiveScene](SceneManagement.SceneManager.SetActiveScene.html)| Set the
Scene to be active.  
[UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html)|
Destroys all GameObjects associated with the given Scene and removes the Scene
from the SceneManager.  
  
### Events

[activeSceneChanged](SceneManagement.SceneManager-activeSceneChanged.html)|
Subscribe to this event to get notified when the active Scene has changed.  
---|---  
[sceneLoaded](SceneManagement.SceneManager-sceneLoaded.html)| Assign a custom
callback to this event to get notifications when a Scene has loaded.  
[sceneUnloaded](SceneManagement.SceneManager-sceneUnloaded.html)| Add a
delegate to this to get notifications when a Scene has unloaded.  
  
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

