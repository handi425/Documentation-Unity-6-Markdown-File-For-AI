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

#  [SceneManager](SceneManagement.SceneManager.html).sceneUnloaded

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

value | Use a subscription of either a UnityAction<[Scene](SceneManagement.Scene.html)> or a method that takes a [Scene](SceneManagement.Scene.html) type argument.  
---|---  
  
### Description

Add a delegate to this to get notifications when a Scene has unloaded.

Rather than being called directly this script code shows use of a delegate.
This means the [sceneUnloaded](SceneManagement.SceneManager-
sceneUnloaded.html) value is added into a list of delegates.  
  
In the script example below a method call is shown. Specifically a function
called OnSceneUnloaded is added to sceneUnloaded. SceneUnloaded is called when
the Scene it is associated with is closed. At this point SceneUnloaded should
be removed from the [sceneUnloaded](SceneManagement.SceneManager-
sceneUnloaded.html) list.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class SceneLoaded1 : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Start()
        {
            [SceneManager.sceneUnloaded](SceneManagement.SceneManager-sceneUnloaded.html) += OnSceneUnloaded;
            [Debug.Log](Debug.Log.html)("Start: SceneLoaded1");
        }  
      
        private void OnSceneUnloaded([Scene](SceneManagement.Scene.html) current)
        {
            [Debug.Log](Debug.Log.html)("OnSceneUnloaded: " + current);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)("space"))
            {
                [Debug.Log](Debug.Log.html)("Quitting Scene1");
                ChangeScene();
            }
        }  
      
        void ChangeScene()
        {
            [Debug.Log](Debug.Log.html)("Changing to Scene2");  
      
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("Scene2");
        }  
      
        void OnDestroy()
        {
            [Debug.Log](Debug.Log.html)("OnDestroy");
        }
    }
    

`SceneLoaded2` simply announces that this is the active Scene.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class SceneLoaded2 : [MonoBehaviour](MonoBehaviour.html)
    {
        public void Start()
        {
            [Debug.Log](Debug.Log.html)("SceneLoaded2");
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

