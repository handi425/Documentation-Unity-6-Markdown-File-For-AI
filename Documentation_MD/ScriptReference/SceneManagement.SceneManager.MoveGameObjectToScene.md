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

#  [SceneManager](SceneManagement.SceneManager.html).MoveGameObjectToScene

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

public static void MoveGameObjectToScene([GameObject](GameObject.html) go,
[SceneManagement.Scene](SceneManagement.Scene.html) scene);

### Parameters

go | GameObject to move.  
---|---  
scene | Scene to move into.  
  
### Description

Move a GameObject from its current Scene to a new Scene.

You can only move root GameObjects from one Scene to another. This means the
GameObject to move must not be a child of any other GameObject in its Scene.
This only works on GameObjects being moved to a Scene that is already loaded
(additive). If you want to load single Scenes, make sure to use
DontDestroyOnLoad on the GameObject you would like to move to a new Scene,
otherwise Unity deletes it when it loads a new Scene.

    
    
    // This script moves the [GameObject](GameObject.html) you attach in the Inspector to a [Scene](SceneManagement.Scene.html) you specify in the Inspector.
    // Attach this script to an empty [GameObject](GameObject.html).
    // Click on the [GameObject](GameObject.html), go to its Inspector and type the name of the [Scene](SceneManagement.Scene.html) you would like to load in the [Scene](SceneManagement.Scene.html) field.
    // Attach the [GameObject](GameObject.html) you would like to move to a new [Scene](SceneManagement.Scene.html) in the "My Game Object" field  
      
    // Make sure your Scenes are in your build (**File** >**Build Settings**).  
      
    using System.Collections;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Type in the name of the [Scene](SceneManagement.Scene.html) you would like to load in the Inspector
        public string m_Scene;  
      
        // Assign your [GameObject](GameObject.html) you want to move [Scene](SceneManagement.Scene.html) in the Inspector
        public [GameObject](GameObject.html) m_MyGameObject;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Press the space key to add the [Scene](SceneManagement.Scene.html) additively and move the [GameObject](GameObject.html) to that [Scene](SceneManagement.Scene.html)
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                StartCoroutine(LoadYourAsyncScene());
            }
        }  
      
        IEnumerator LoadYourAsyncScene()
        {
            // Set the current [Scene](SceneManagement.Scene.html) to be able to unload it later
            [Scene](SceneManagement.Scene.html) currentScene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();  
      
            // The [Application](Application.html) loads the [Scene](SceneManagement.Scene.html) in the background at the same time as the current [Scene](SceneManagement.Scene.html).
            [AsyncOperation](AsyncOperation.html) asyncLoad = [SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)(m_Scene, [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));  
      
            // Wait until the last operation fully loads to return anything
            while (!asyncLoad.isDone)
            {
                yield return null;
            }  
      
            // Move the [GameObject](GameObject.html) (you attach this in the Inspector) to the newly loaded [Scene](SceneManagement.Scene.html)
            [SceneManager.MoveGameObjectToScene](SceneManagement.SceneManager.MoveGameObjectToScene.html)(m_MyGameObject, [SceneManager.GetSceneByName](SceneManagement.SceneManager.GetSceneByName.html)(m_Scene));
            // Unload the previous [Scene](SceneManagement.Scene.html)
            [SceneManager.UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html)(currentScene);
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

