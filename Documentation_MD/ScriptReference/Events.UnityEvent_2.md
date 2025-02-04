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

# UnityEvent<T0,T1>

class in UnityEngine.Events

/

Inherits from:[Events.UnityEventBase](Events.UnityEventBase.html)

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

Two argument version of [UnityEvent](Events.UnityEvent.html).

Generics are supported, specify type parameters on initialization as shown in
the example. Refer to [Configure callbacks in the
Inspector](../Manual/UnityEvents.html) for details on configuring callbacks in
the Inspector window.

    
    
    using UnityEngine;
    using UnityEngine.Events;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [UnityEvent](Events.UnityEvent.html)<int, int> m_MyEvent;  
      
        void Start()
        {
            if (m_MyEvent == null)
                m_MyEvent = new [UnityEvent](Events.UnityEvent.html)<int, int>();  
      
            m_MyEvent.AddListener(DoSomething);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.anyKeyDown](Input-anyKeyDown.html) && m_MyEvent != null)
            {
                m_MyEvent.Invoke(5, 6);
            }
        }  
      
        void DoSomething(int i, int j)
        {
            [Debug.Log](Debug.Log.html)("Callback called " + i + ", " + j);
        }
    }
    

Note: UnityEvent can also be awaited in any async method.

### Inherited Members

### Public Methods

[GetPersistentEventCount](Events.UnityEventBase.GetPersistentEventCount.html)|
Get the number of registered persistent listeners.  
---|---  
[GetPersistentListenerState](Events.UnityEventBase.GetPersistentListenerState.html)|
Returns the execution state of a persistent listener.  
[GetPersistentMethodName](Events.UnityEventBase.GetPersistentMethodName.html)|
Get the target method name of the listener at index index.  
[GetPersistentTarget](Events.UnityEventBase.GetPersistentTarget.html)| Get the
target component of the listener at index index.  
[RemoveAllListeners](Events.UnityEventBase.RemoveAllListeners.html)| Remove
all non-persistent (ie created from script) listeners from the event.  
[SetPersistentListenerState](Events.UnityEventBase.SetPersistentListenerState.html)|
Modify the execution state of a persistent listener.  
  
### Static Methods

[GetValidMethodInfo](Events.UnityEventBase.GetValidMethodInfo.html)| Given an
object, function name, and a list of argument types; find the method that
matches.  
---|---  
  
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

