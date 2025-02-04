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

#  [SceneManager](SceneManagement.SceneManager.html).LoadSceneAsync

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

public static [AsyncOperation](AsyncOperation.html) LoadSceneAsync(string
sceneName, [SceneManagement.LoadSceneMode](SceneManagement.LoadSceneMode.html)
mode = LoadSceneMode.Single);

## Declaration

public static [AsyncOperation](AsyncOperation.html) LoadSceneAsync(int
sceneBuildIndex,
[SceneManagement.LoadSceneMode](SceneManagement.LoadSceneMode.html) mode =
LoadSceneMode.Single);

## Declaration

public static [AsyncOperation](AsyncOperation.html) LoadSceneAsync(string
sceneName,
[SceneManagement.LoadSceneParameters](SceneManagement.LoadSceneParameters.html)
parameters);

## Declaration

public static [AsyncOperation](AsyncOperation.html) LoadSceneAsync(int
sceneBuildIndex,
[SceneManagement.LoadSceneParameters](SceneManagement.LoadSceneParameters.html)
parameters);

### Parameters

sceneName | Name or path of the Scene to load.  
---|---  
sceneBuildIndex | Index of the Scene in the Build Settings to load.  
mode | If LoadSceneMode.Single then all current Scenes will be unloaded before loading.  
parameters | Struct that collects the various parameters into a single place except for the name and index.  
  
### Returns

**AsyncOperation** Use the [AsyncOperation](AsyncOperation.html) to determine
if the operation has completed.

### Description

Loads the Scene asynchronously in the background.

You can provide the full Scene path, the path shown in the Build Settings
window, or just the Scene name. If you only provide the Scene name, Unity
loads the first Scene in the list that matches. If you have multiple Scenes
with the same name but different paths, you should use the full Scene path in
the Build Settings.  
  
Examples of supported formats:  
`"Scene1"`  
`"Scenes/Scene1"`  
`"Scenes/Others/Scene1"`  
`"Assets/scenes/others/scene1.unity"`  
  
**Note:** Scene name input is not case-sensitive.  
If you call this method with an invalid **sceneName** or **sceneBuildIndex** ,
Unity throws an exception.  
  
**Note:** The name of the Scene to load can be case insensitive.  
  
If a single mode scene is loaded, Unity calls Resources.UnloadUnusedAssets
automatically.

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Press the space key to start coroutine
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                // Use a coroutine to load the [Scene](SceneManagement.Scene.html) in the background
                StartCoroutine(LoadYourAsyncScene());
            }
        }  
      
        IEnumerator LoadYourAsyncScene()
        {
            // The [Application](Application.html) loads the [Scene](SceneManagement.Scene.html) in the background as the current [Scene](SceneManagement.Scene.html) runs.
            // This is particularly good for creating loading screens.
            // You could also load the [Scene](SceneManagement.Scene.html) by using sceneBuildIndex. In this case Scene2 has
            // a sceneBuildIndex of 1 as shown in Build [Settings](Rendering.RayTracingAccelerationStructure.Settings.html).  
      
            [AsyncOperation](AsyncOperation.html) asyncLoad = [SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)("Scene2");  
      
            // Wait until the asynchronous scene fully loads
            while (!asyncLoad.isDone)
            {
                yield return null;
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

