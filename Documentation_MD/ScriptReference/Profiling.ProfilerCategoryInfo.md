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

# ProfilerCategoryInfo

struct in UnityEditor.Profiling

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

Category information descriptor structure.

Contains the full information about a Profiler category such as its name,
color, id, and flags. Use with
[FrameDataView.GetAllCategories](Profiling.FrameDataView.GetAllCategories.html)
and
[FrameDataView.GetCategoryInfo](Profiling.FrameDataView.GetCategoryInfo.html)
to get information on the available Profiler categories.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using UnityEditor.Profiling;
    using Unity.Profiling;  
      
    public class Example
    {
        public static void GetAllBuiltinProfilerCategories([FrameDataView](Profiling.FrameDataView.html) frameDataView, List<[ProfilerCategoryInfo](Profiling.ProfilerCategoryInfo.html)> unityProfilerCategories)
        {
            unityProfilerCategories.Clear();
            var infos = new List<[ProfilerCategoryInfo](Profiling.ProfilerCategoryInfo.html)>();
            frameDataView.GetAllCategories(infos);
            foreach (var info in infos)
            {
                if (info.flags.HasFlag([ProfilerCategoryFlags.Builtin](Unity.Profiling.ProfilerCategoryFlags.Builtin.html)))
                {
                    unityProfilerCategories.Add(info);
                }
            }
        }
    }
    

### Properties

[color](Profiling.ProfilerCategoryInfo-color.html)| The color of the Profiler
category, as a Color32.  
---|---  
[flags](Profiling.ProfilerCategoryInfo-flags.html)| Flags for showing if the
Category is user defined or built into Unity.  
[id](Profiling.ProfilerCategoryInfo-id.html)| Id used by Unity for tracking
the Category.  
[name](Profiling.ProfilerCategoryInfo-name.html)| The name used by Unity for
the Category.  
  
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

