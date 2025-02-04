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

#  [Application](Application.html).memoryUsageChanged

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

Informs about significant changes in the application's memory usage.

This event occurs when there are significant changes in the application's
memory usage, such as an increase to a dangerous level or a drop to a much
safer level.  
  
You can use this event to balance your application's memory usage for device
capability. For example, you can lower the resource intensity of your
application when memory usage becomes critical.  
  
iOS, Android, and Universal Windows Platform (UWP) support this event, but not
every platform supports all possible
[ApplicationMemoryUsage](ApplicationMemoryUsage.html) values.

  * Android supports [Medium](ApplicationMemoryUsage.Medium.html), [High](ApplicationMemoryUsage.High.html), and [Critical](ApplicationMemoryUsage.Critical.html).   
**Note:** When targeting
[GameActivity](https://developer.android.com/games/agdk/game-activity), only
[Critical](ApplicationMemoryUsage.Critical.html) is supported.

  * iOS supports [Critical](ApplicationMemoryUsage.Critical.html).
  * UWP supports [Low](ApplicationMemoryUsage.Low.html), [Medium](ApplicationMemoryUsage.Medium.html), [High](ApplicationMemoryUsage.High.html), and [Critical](ApplicationMemoryUsage.Critical.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;  
      
    public class [Sample](PackageManager.UI.Sample.html) : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Application.memoryUsageChanged](Application-memoryUsageChanged.html) += OnMemoryUsageChanged;
        }  
      
        void OnMemoryUsageChanged(in [ApplicationMemoryUsageChange](ApplicationMemoryUsageChange.html) newUsage)
        {
            if (newUsage.memoryUsage == [ApplicationMemoryUsage.Critical](ApplicationMemoryUsage.Critical.html))
            {
                // release resources here
                [Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html)();
                GC.Collect();
            }
        }
    }
    

This code sample shows how to perform garbage collection if the application is
critically low on memory.

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

