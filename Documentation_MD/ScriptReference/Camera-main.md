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

#  [Camera](Camera.html).main

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

public static [Camera](Camera.html) main;

### Description

The first enabled Camera component that is tagged "MainCamera" (Read Only).

If there is no enabled Camera component with the "MainCamera" tag, this
property is null.  
  
Internally, Unity caches all GameObjects with the "MainCamera" tag. When you
access this property, Unity returns the first valid result from its cache.
Accessing this property has a small CPU overhead, comparable to calling
[GameObject.GetComponent](GameObject.GetComponent.html). Where CPU performance
is important, consider caching this property.  
  
Additional resources: [Tags](../Manual/Tags.html)

    
    
    //Place this script on a [GameObject](GameObject.html) to switch between the main [Camera](Camera.html) and your own second [Camera](Camera.html) on the press of the "L" key
    //Place a second [Camera](Camera.html) in your [Scene](SceneManagement.Scene.html) and assign it as the "[Camera](Camera.html) Two" in the Inspector.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //This is Main [Camera](Camera.html) in the [Scene](SceneManagement.Scene.html)
        [Camera](Camera.html) m_MainCamera;
        //This is the second [Camera](Camera.html) and is assigned in inspector
        public [Camera](Camera.html) m_CameraTwo;  
      
        void Start()
        {
            //This gets the Main [Camera](Camera.html) from the [Scene](SceneManagement.Scene.html)
            m_MainCamera = [Camera.main](Camera-main.html);
            //This enables Main [Camera](Camera.html)
            m_MainCamera.enabled = true;
            //Use this to disable secondary [Camera](Camera.html)
            m_CameraTwo.enabled = false;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the L [Button](UIElements.Button.html) to switch cameras
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.L](KeyCode.L.html)))
            {
                //Check that the Main [Camera](Camera.html) is enabled in the [Scene](SceneManagement.Scene.html), then switch to the other [Camera](Camera.html) on a key press
                if (m_MainCamera.enabled)
                {
                    //Enable the second [Camera](Camera.html)
                    m_CameraTwo.enabled = true;  
      
                    //The Main first [Camera](Camera.html) is disabled
                    m_MainCamera.enabled = false;
                }
                //Otherwise, if the Main [Camera](Camera.html) is not enabled, switch back to the Main [Camera](Camera.html) on a key press
                else if (!m_MainCamera.enabled)
                {
                    //Disable the second camera
                    m_CameraTwo.enabled = false;  
      
                    //Enable the Main [Camera](Camera.html)
                    m_MainCamera.enabled = true;
                }
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

