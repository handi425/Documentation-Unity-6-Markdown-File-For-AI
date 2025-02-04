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

#  [SceneManager](SceneManagement.SceneManager.html).sceneLoaded

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

### Parameters

value | A method with the signature MyMethod([Scene](SceneManagement.Scene.html), [LoadSceneMode](SceneManagement.LoadSceneMode.html)).  
---|---  
  
### Description

Assign a custom callback to this event to get notifications when a Scene has
loaded.

Create a custom callback method to receive the notification and assign it to
the `SceneManager.sceneLoaded` event. The callback must have the required
signature, taking a [Scene](SceneManagement.Scene.html) and a
[LoadSceneMode](SceneManagement.LoadSceneMode.html) as input parameters.  
  
The code example below defines a custom calllback method called
`OnSceneLoaded` with the required signature. It assigns `OnSceneLoaded` to
`SceneManager.sceneLoaded` in the `OnEnable` callback and unassigns it in the
`OnDisable` callback.  
  
The code example and comment annotations demonstrate the execution order of
the callbacks. Unity raises the `SceneManager.sceneLoaded` event and invokes
the associated callback after `OnEnable` but before `Start`.  
  
Additional resources: [Details of disabling domain and scene
reload](../Manual/configurable-enter-play-mode-details.html)

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class ExampleCode : [MonoBehaviour](MonoBehaviour.html)
    {
        // called first
        void Awake()
        {
            [Debug.Log](Debug.Log.html)("Awake");
        }  
      
        // called second
        void OnEnable()
        {
            [Debug.Log](Debug.Log.html)("OnEnable called");
            [SceneManager.sceneLoaded](SceneManagement.SceneManager-sceneLoaded.html) += OnSceneLoaded;
        }  
      
        // called third
        void OnSceneLoaded([Scene](SceneManagement.Scene.html) scene, [LoadSceneMode](SceneManagement.LoadSceneMode.html) mode)
        {
            [Debug.Log](Debug.Log.html)("OnSceneLoaded: " + scene.name);
            [Debug.Log](Debug.Log.html)(mode);
        }  
      
        // called fourth
        void Start()
        {
            [Debug.Log](Debug.Log.html)("Start");
        }  
      
        // called when the game is terminated
        void OnDisable()
        {
            [Debug.Log](Debug.Log.html)("OnDisable");
            [SceneManager.sceneLoaded](SceneManagement.SceneManager-sceneLoaded.html) -= OnSceneLoaded;
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

