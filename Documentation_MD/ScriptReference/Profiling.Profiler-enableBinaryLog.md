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

#  [Profiler](Profiling.Profiler.html).enableBinaryLog

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

public static bool enableBinaryLog;

### Description

Enables the logging of profiling data to a file.

When enabled, the Unity player saves profiling data to the file specified in
the [Profiler.logFile](Profiling.Profiler-logFile.html) file. The player
automatically assigns the file extension, “.raw” to this log file. You can
load this file in the Unity Editor using the Profiler window to view the data.  
  
You must also set [Profiler.enabled](Profiling.Profiler-enabled.html) to
`true`. If the buffer is too small to output the profiler data you will see a
message in the debug log "Skipping profile frame. Receiver can not keep up
with the amount of data sent". Use
[Profiler.maxUsedMemory](Profiling.Profiler-maxUsedMemory.html) to raise the
buffer memory.  
  
**Note:** In the following example, on the WebGL platform, the log file is
outputted to a path like the following: `/idbfs/some-hash/profiler.raw`. To
find this file, use your browser's developer tools. You can also use
`File.Open` with the same path that you used to load the data, and use
[UnityWebRequest.Post](Networking.UnityWebRequest.Post.html) to send it to a
web server.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Profiling;
    using System.IO;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(RunProfiler());
        }  
      
        IEnumerator RunProfiler()
        {
            // Specify the profiler output file
            [Profiler.logFile](Profiling.Profiler-logFile.html) = Path.Join([Application.persistentDataPath](Application-persistentDataPath.html), "mylog.raw");
            [Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) = true;
            // Start profiler
            [Profiler.enabled](Profiling.Profiler-enabled.html) = true;
            // Optional, if more memory is needed for the buffer
            [Profiler.maxUsedMemory](Profiling.Profiler-maxUsedMemory.html) = 256 * 1024 * 1024;  
      
            // Run profiling for 5 seconds
            yield return new [WaitForSeconds](WaitForSeconds.html)(5.0f);  
      
            // Stop profiler
            [Profiler.enabled](Profiling.Profiler-enabled.html) = false;
            // It is important to change the log file so it can be opened
            [Profiler.logFile](Profiling.Profiler-logFile.html) = "";
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

