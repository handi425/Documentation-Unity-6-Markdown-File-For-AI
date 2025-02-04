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

# ILogHandler

interface in UnityEngine

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

Interface for custom log handler implementation.

ILogHandler interface to ease unit-testing and mocking of loggers.

    
    
    using UnityEngine;
    using System.Collections;
    using System.IO;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    public class MyFileLogHandler : [ILogHandler](ILogHandler.html)
    {
        private FileStream m_FileStream;
        private StreamWriter m_StreamWriter;
        private [ILogHandler](ILogHandler.html) m_DefaultLogHandler = Debug.unityLogger.logHandler;  
      
        public MyFileLogHandler()
        {
            string filePath = [Application.persistentDataPath](Application-persistentDataPath.html) + "/MyLogs.txt";  
      
            m_FileStream = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.ReadWrite);
            m_StreamWriter = new StreamWriter(m_FileStream);  
      
            // Replace the default debug log handler
            Debug.unityLogger.logHandler = this;
        }  
      
        public void LogFormat([LogType](LogType.html) logType, UnityEngine.Object context, string format, params object[] args)
        {
            m_StreamWriter.WriteLine(String.Format(format, args));
            m_StreamWriter.Flush();
            m_DefaultLogHandler.LogFormat(logType, context, format, args);
        }  
      
        public void LogException(Exception exception, UnityEngine.Object context)
        {
            m_DefaultLogHandler.LogException(exception, context);
        }
    }  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private static [ILogger](ILogger.html) logger = [Debug.unityLogger](Debug-unityLogger.html);
        private static string kTAG = "MyGameTag";
        private MyFileLogHandler myFileLogHandler;  
      
        void Start()
        {
            myFileLogHandler = new MyFileLogHandler();  
      
            logger.Log(kTAG, "MyGameClass Start.");
        }
    }
    

### Public Methods

[LogException](ILogHandler.LogException.html)| A variant of
ILogHandler.LogFormat that logs an exception message.  
---|---  
[LogFormat](ILogHandler.LogFormat.html)| Logs a formatted message.  
  
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

