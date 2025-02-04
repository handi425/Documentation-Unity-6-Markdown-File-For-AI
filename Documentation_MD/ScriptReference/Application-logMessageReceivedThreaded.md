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

#  [Application](Application.html).logMessageReceivedThreaded

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

Event that is fired if a log message is received.

This event will be triggered regardless of whether the message comes in on the
main thread or not. This means that the handler code has to be thread-safe. It
may be invoked from different threads and may be invoked in parallel. Make
sure to only access Unity APIs from your handlers that are allowed to be
called from threads other than the main thread.  
  
**Note:** It is not necessary to subscribe to both
[Application.logMessageReceived](Application-logMessageReceived.html) and
`Application.logMessageReceivedThreaded`. The multi-threaded variant will also
be called for messages on the main thread.  
  
Additional resources: [Application.logMessageReceived](Application-
logMessageReceived.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string output = "";
        public string stack = "";  
      
        void OnEnable()
        {
            [Application.logMessageReceivedThreaded](Application-logMessageReceivedThreaded.html) += HandleLog;
        }  
      
        void OnDisable()
        {
            [Application.logMessageReceivedThreaded](Application-logMessageReceivedThreaded.html) -= HandleLog;
        }  
      
        void HandleLog(string logString, string stackTrace, [LogType](LogType.html) type)
        {
            output = logString;
            stack = stackTrace;
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

