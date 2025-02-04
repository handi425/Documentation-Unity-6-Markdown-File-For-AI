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

#  [AssetDatabase](AssetDatabase.html).IsDirectoryMonitoringEnabled

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

public static bool IsDirectoryMonitoringEnabled();

### Returns

**bool** Returns true when Directory Monitoring is enabled. Returns false
otherwise.

### Description

Reports whether Directory Monitoring is enabled.

Turn Directory Monitoring on or off in Preferences settings or in script with
EditorPrefs.SetBool("DirectoryMonitoring", boolValue).  
Directory Monitoring can be disabled with command line flag
[[-DisableDirectoryMonitor]] and Directory Monitoring is automatically
disabled when Unity detects symlinks in the project.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.Profiling;
    using System.IO;  
      
    public class DirectoryMonitoringTest
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/[Directory](Windows.Directory.html) Monitoring Test")]
        static void DirectoryMonitoringBenchmark()
        {
            var BenchmarkCount = 1;  
      
            //Disabling the [Directory](Windows.Directory.html) Monitoring will use a brute force scanning method to evaluate which files in the project have been changed, and is much slower
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("DirectoryMonitoring", false);
            [Debug.Log](Debug.Log.html)("Is [Directory](Windows.Directory.html) Monitoring Enabled? - " + [AssetDatabase.IsDirectoryMonitoringEnabled](AssetDatabase.IsDirectoryMonitoringEnabled.html)());  
      
            Benchmark(BenchmarkCount);
            BenchmarkCount++;  
      
            [EditorPrefs.SetBool](EditorPrefs.SetBool.html)("DirectoryMonitoring", true);
            [Debug.Log](Debug.Log.html)("Is [Directory](Windows.Directory.html) Monitoring Enabled? - " + [AssetDatabase.IsDirectoryMonitoringEnabled](AssetDatabase.IsDirectoryMonitoringEnabled.html)());
            Benchmark(BenchmarkCount);
        }  
      
        //This test will show faster scan time when using [Directory](Windows.Directory.html) Monitoring
        static void Benchmark(int BenchmarkCount)
        {
            var relativePath = "Assets/test_file01.txt";
            if (![File.Exists](Windows.File.Exists.html)(relativePath))
            {
                using (StreamWriter sw = File.CreateText(relativePath))
                {
                    sw.WriteLine("Hello");
                    sw.WriteLine("And");
                    sw.WriteLine("Welcome");
                }
            }  
      
            [Profiler.BeginSample](Profiling.Profiler.BeginSample.html)("Benchmark " + BenchmarkCount); ;
            [AssetDatabase.ImportAsset](AssetDatabase.ImportAsset.html)(relativePath);
            [Profiler.EndSample](Profiling.Profiler.EndSample.html)();  
      
            [AssetDatabase.DeleteAsset](AssetDatabase.DeleteAsset.html)(relativePath);
            [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
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

