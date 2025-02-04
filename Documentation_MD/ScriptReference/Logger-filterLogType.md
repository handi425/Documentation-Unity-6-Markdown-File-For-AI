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

#  [Logger](Logger.html).filterLogType

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

public [LogType](LogType.html) filterLogType;

### Description

To selective enable debug log message.

By settings filterLogType to  
  
[LogType.Log](LogType.Log.html) (default setting) will display all log
messages.  
  
[LogType.Warning](LogType.Warning.html) will display Warning, Assert, Error
and Exception log messages.  
  
[LogType.Assert](LogType.Assert.html) will display Assert, Error and Exception
log messages.  
  
[LogType.Error](LogType.Error.html) will display Error and Exception log
messages.  
  
[LogType.Exception](LogType.Exception.html) will display Exception log
messages.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private static [ILogger](ILogger.html) logger = [Debug.unityLogger](Debug-unityLogger.html);
        private static string kTAG = "MyGameTag";  
      
        void Start()
        {
            if ([Debug.isDebugBuild](Debug-isDebugBuild.html))
                logger.filterLogType = [LogType.Log](LogType.Log.html);
            else
                logger.filterLogType = [LogType.Warning](LogType.Warning.html);  
      
            logger.Log(kTAG, "This log will be displayed only in debug build");
            logger.LogError(kTAG, "This log will be displayed in debug and release build");
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

