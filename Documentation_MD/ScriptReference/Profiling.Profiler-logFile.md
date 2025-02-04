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

#  [Profiler](Profiling.Profiler.html).logFile

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

public static string logFile;

### Description

Specifies the file to use when writing profiling data.

In addition to specifying a valid file path, you must set both
[Profiler.enabled](Profiling.Profiler-enabled.html) and
[Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) to `true`
in order to save profiling information. Specifying a new valid file path while
[Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) is `true`
will save profiling information to that file instead. If a `null` or an empty
path is passed [Profiler.enableBinaryLog](Profiling.Profiler-
enableBinaryLog.html) will automatically be set to `false`.  
  
When using the relative log file path, the directory on each platform is set
to [Application.dataPath](Application-dataPath.html), apart from WebGL, which
uses [Application.persistentDataPath](Application-persistentDataPath.html).  
  
If the buffer is too small to output the profiler data you will see a message
in the debug log "Skipping profile frame. Receiver can not keep up with the
amount of data sent". Use [Profiler.maxUsedMemory](Profiling.Profiler-
maxUsedMemory.html) to raise the buffer memory.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Profiling;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Profiler.logFile](Profiling.Profiler-logFile.html) = "mylog"; //Also supports passing "myLog.raw"
            [Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) = true;
            [Profiler.enabled](Profiling.Profiler-enabled.html) = true;  
      
            // Optional, if more memory is needed for the buffer
            [Profiler.maxUsedMemory](Profiling.Profiler-maxUsedMemory.html) = 256 * 1024 * 1024;  
      
            // ...  
      
            // Optional, to close the file when done
            [Profiler.enabled](Profiling.Profiler-enabled.html) = false;
            [Profiler.logFile](Profiling.Profiler-logFile.html) = "";  
      
            // To start writing to a new log file
            [Profiler.logFile](Profiling.Profiler-logFile.html) = "myOtherLog";
            [Profiler.enabled](Profiling.Profiler-enabled.html) = true;
            // ...
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

