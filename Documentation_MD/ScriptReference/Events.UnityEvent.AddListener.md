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

#  [UnityEvent](Events.UnityEvent.html).AddListener

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

public void AddListener([Events.UnityAction](Events.UnityAction.html) call);

### Parameters

call | Callback function.  
---|---  
  
### Description

Adds a non-persistent listener to the UnityEvent.

Adds a runtime callback. You can add many different listeners. If you add
identical listeners multiple times, it results in only one call being made to
that specific listener.

    
    
    //Attach this script to a [GameObject](GameObject.html)
    //This script creates a [UnityEvent](Events.UnityEvent.html) that calls a method when a key is pressed
    //Note that 'q' exits this application.
    using UnityEngine;
    using UnityEngine.Events;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [UnityEvent](Events.UnityEvent.html) m_MyEvent = new [UnityEvent](Events.UnityEvent.html)();  
      
        void Start()
        {
            //Add a listener to the new [Event](Event.html). Calls MyAction method when invoked
            m_MyEvent.AddListener(MyAction);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Press Q to close the Listener
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("q") && m_MyEvent != null)
            {
                [Debug.Log](Debug.Log.html)("Quitting");
                m_MyEvent.RemoveListener(MyAction);  
      
                #if UNITY_EDITOR
                UnityEditor.EditorApplication.isPlaying = false;
                #endif  
      
                [Application.Quit](Application.Quit.html)();
            }  
      
            //Press any other key to begin the action if the [Event](Event.html) exists
            if ([Input.anyKeyDown](Input-anyKeyDown.html) && m_MyEvent != null)
            {
                //Begin the action
                m_MyEvent.Invoke();
            }
        }  
      
        void MyAction()
        {
            //Output message to the console
            [Debug.Log](Debug.Log.html)("Do Stuff");
        }
    }
    

Additional resources:
[UnityEventTools.AddPersistentListener](Events.UnityEventTools.AddPersistentListener.html).

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

