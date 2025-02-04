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

# ILogger

interface in UnityEngine

Leave feedback

  

Implements interfaces:[ILogHandler](ILogHandler.html)

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

Interface for custom logger implementation.

Additional resources: [Logger](Logger.html), [Debug.unityLogger](Debug-
unityLogger.html) [ILogHandler](ILogHandler.html).

### Properties

[filterLogType](ILogger-filterLogType.html)| To selective enable debug log
message.  
---|---  
[logEnabled](ILogger-logEnabled.html)| To runtime toggle debug logging
[ON/OFF].  
[logHandler](ILogger-logHandler.html)| Set Logger.ILogHandler.  
  
### Public Methods

[IsLogTypeAllowed](ILogger.IsLogTypeAllowed.html)| Check logging is enabled
based on the LogType.  
---|---  
[Log](ILogger.Log.html)| Logs message to the Unity Console using default
logger.  
[LogError](ILogger.LogError.html)| A variant of ILogger.Log that logs an error
message.  
[LogException](ILogger.LogException.html)| A variant of ILogger.Log that logs
an exception message.  
[LogFormat](ILogger.LogFormat.html)| Logs a formatted message.  
[LogWarning](ILogger.LogWarning.html)| A variant of Logger.Log that logs an
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

