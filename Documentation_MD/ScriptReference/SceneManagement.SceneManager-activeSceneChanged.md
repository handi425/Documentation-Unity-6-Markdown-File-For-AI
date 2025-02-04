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

#  [SceneManager](SceneManagement.SceneManager.html).activeSceneChanged

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

value | Use a subscription of either a UnityAction<[Scene](SceneManagement.Scene.html), [Scene](SceneManagement.Scene.html)> or a method that takes two [Scene](SceneManagement.Scene.html) types arguments.  
---|---  
  
### Description

Subscribe to this event to get notified when the active Scene has changed.

This script added to [activeSceneChanged](SceneManagement.SceneManager-
activeSceneChanged.html) takes two hidden arguments. These are the replaced
Scene and the next Scene. The arguments are not visible.  
  
In the Editor this event is sent only in Play mode (not in Edit mode). If the
event is needed for Edit mode then use
[EditorSceneManager.activeSceneChangedInEditMode](SceneManagement.EditorSceneManager-
activeSceneChangedInEditMode.html).

    
    
    // [SceneManager.activeSceneChanged](SceneManagement.SceneManager-activeSceneChanged.html)
    //
    // This example configures Scene1 to wait for 1.5 seconds before switching to Scene2.
    // Scene1 is the replaced [Scene](SceneManagement.Scene.html); Scene2 is the new loaded [Scene](SceneManagement.Scene.html).  
      
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class ScriptExample1 : [MonoBehaviour](MonoBehaviour.html)
    {
        public delegate void Change();
        public static event Change TimeChanged;  
      
        public void Start()
        {
            [SceneManager.activeSceneChanged](SceneManagement.SceneManager-activeSceneChanged.html) += ChangedActiveScene;  
      
            // wait 1.5 seconds before change to Scene2
            StartCoroutine(TimeChangedScene());
        }  
      
        IEnumerator TimeChangedScene()
        {
            print([Time.time](Time-time.html) + " seconds");
            yield return new [WaitForSeconds](WaitForSeconds.html)(1.5f);
            print([Time.time](Time-time.html) + " seconds");  
      
            // call the event
            TimeChanged();
        }  
      
        private void ChangedActiveScene([Scene](SceneManagement.Scene.html) current, [Scene](SceneManagement.Scene.html) next)
        {
            string currentName = current.name;  
      
            if (currentName == null)
            {
                // Scene1 has been removed
                currentName = "Replaced";
            }  
      
            [Debug.Log](Debug.Log.html)("Scenes: " + currentName + ", " + next.name);
        }  
      
        void OnEnable()
        {
            [Debug.Log](Debug.Log.html)("OnEnable");
            ScriptExample1.TimeChanged += ChangeScene;
        }  
      
        void ChangeScene()
        {
            [Debug.Log](Debug.Log.html)("Changing to Scene2");
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("Scene2");  
      
            [Scene](SceneManagement.Scene.html) scene = [SceneManager.GetSceneByName](SceneManagement.SceneManager.GetSceneByName.html)("Scene2");
            [SceneManager.SetActiveScene](SceneManagement.SceneManager.SetActiveScene.html)(scene);
        }  
      
        void OnDisable()
        {
            ScriptExample1.TimeChanged -= ChangeScene;
            [Debug.Log](Debug.Log.html)("OnDisable happened for Scene1");
        }
    }
    

`ScriptExample2` simply announces that this is the active Scene.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class ScriptExample2 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)("Script2 starting");
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

