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

# Logger

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

  

Implements interfaces:[ILogger](ILogger.html), [ILogHandler](ILogHandler.html)

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

Initializes a new instance of the Logger.

Create a new instance or use default [Debug.unityLogger](Debug-
unityLogger.html). Additional resources: [ILogger](ILogger.html),
[ILogHandler](ILogHandler.html).

    
    
    using UnityEngine;
    using System.Collections;
    using System.IO;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    public class MyLogHandler : [ILogHandler](ILogHandler.html)
    {
        public void LogFormat([LogType](LogType.html) logType, UnityEngine.Object context, string format, params object[] args)
        {
            Debug.unityLogger.logHandler.LogFormat(logType, context, format, args);
        }  
      
        public void LogException(Exception exception, UnityEngine.Object context)
        {
            Debug.unityLogger.LogException(exception, context);
        }
    }  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private static string kTAG = "MyGameTag";
        private [Logger](Logger.html) myLogger;  
      
        void Start()
        {
            myLogger = new [Logger](Logger.html)(new MyLogHandler());  
      
            myLogger.Log(kTAG, "MyGameClass Start.");
        }
    }
    

### Properties

[filterLogType](Logger-filterLogType.html)| To selective enable debug log
message.  
---|---  
[logEnabled](Logger-logEnabled.html)| To runtime toggle debug logging
[ON/OFF].  
[logHandler](Logger-logHandler.html)| Set Logger.ILogHandler.  
  
### Constructors

[Logger](Logger-ctor.html)| Create a custom Logger.  
---|---  
  
### Public Methods

[IsLogTypeAllowed](Logger.IsLogTypeAllowed.html)| Check logging is enabled
based on the LogType.  
---|---  
[Log](Logger.Log.html)| Logs message to the Unity Console using default
logger.  
[LogError](Logger.LogError.html)| A variant of Logger.Log that logs an error
message.  
[LogException](Logger.LogException.html)| A variant of Logger.Log that logs an
exception message.  
[LogFormat](Logger.LogFormat.html)| Logs a formatted message.  
[LogWarning](Logger.LogWarning.html)| A variant of Logger.Log that logs an
warning message.  
  
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

