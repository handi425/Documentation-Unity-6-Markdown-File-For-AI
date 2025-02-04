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

#
[ProfilerRecorderHandle](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html).GetAvailable

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

public static void GetAvailable(List<ProfilerRecorderHandle>
outRecorderHandleList);

### Description

Gets all available handles which can be accessed with ProfilerRecorder.

Enumerates all available built-in or dynamically created handles of Profiler
markers and counters.

    
    
    using System.Collections.Generic;
    using System.Text;
    using UnityEngine;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public class Example
    {
        struct StatInfo
        {
            public [ProfilerCategory](Unity.Profiling.ProfilerCategory.html) Cat;
            public string Name;
            public [ProfilerMarkerDataUnit](Unity.Profiling.ProfilerMarkerDataUnit.html) [Unit](Unity.Android.Gradle.Manifest.Unit.html);
        }  
      
        static unsafe void EnumerateProfilerStats()
        {
            var availableStatHandles = new List<[ProfilerRecorderHandle](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html)>();
            [ProfilerRecorderHandle.GetAvailable](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html)(availableStatHandles);  
      
            var availableStats = new List<StatInfo>(availableStatHandles.Count);
            foreach (var h in availableStatHandles)
            {
                var statDesc = [ProfilerRecorderHandle.GetDescription](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetDescription.html)(h);
                var statInfo = new StatInfo()
                {
                    Cat = statDesc.Category,
                    Name = statDesc.Name,
                    [Unit](Unity.Android.Gradle.Manifest.Unit.html) = statDesc.UnitType
                };
                availableStats.Add(statInfo);
            }
            availableStats.Sort((a, b) =>
            {
                var result = string.Compare(a.Cat.ToString(), b.Cat.ToString());
                if (result != 0)
                    return result;  
      
                return string.Compare(a.Name, b.Name);
            });  
      
            var sb = new StringBuilder("Available stats:\n");
            foreach (var s in availableStats)
            {
                sb.AppendLine($"{(int)s.Cat}\t\t - {s.Name}\t\t - {s.Unit}");
            }  
      
            [Debug.Log](Debug.Log.html)(sb.ToString());
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

