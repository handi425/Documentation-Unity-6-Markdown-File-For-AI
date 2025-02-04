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

#  [XRStats](XR.Provider.XRStats.html).TryGetStat

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

public static bool TryGetStat([IntegratedSubsystem](IntegratedSubsystem.html)
xrSubsystem, string tag, out float value);

### Parameters

xrSubsystem | The subsystem with which the stat is registered.  
---|---  
tag | The tag used to query for a statistic.  
value | Receives the current value of the requested statistic. Contains a valid value when this method returns true.  
  
### Returns

**bool** True, if the requested statistic is available, false otherwise.

### Description

Retrieve a statistic for an XR subsystem.

The TryGetStat method queries an XR subsystem for the specified statistic and,
if available, sets the output `value` parameter to the current statistic
value. TryGetStat returns true to indicate that the output parameter contains
a valid statistic value. If the specified tag is not defined for the subsystem
or the subsystem itself is not ready, TryGetStat returns false.

    
    
    using UnityEngine.XR.Provider;
    using System.Collections.Generic;
    using UnityEngine.XR;
    using UnityEngine;
    using [XRStats](XR.Provider.XRStats.html) = UnityEngine.XR.Provider.XRStats;  
      
    public static class OpenVRStats
    {
        public static float GPUFrameTime()
        {
            float tmp;
            [XRStats.TryGetStat](XR.Provider.XRStats.TryGetStat.html)(GetFirstDisplaySubsystem(), "OpenVR.Display.GPUFrameTime", out tmp);
            return tmp;
        }  
      
        public static float MotionToPhoton()
        {
            float tmp;
            [XRStats.TryGetStat](XR.Provider.XRStats.TryGetStat.html)(GetFirstDisplaySubsystem(), "MotionToPhoton", out tmp);
            return tmp;
        }  
      
        // etc...
        private static [IntegratedSubsystem](IntegratedSubsystem.html) GetFirstDisplaySubsystem()
        {
            List<[XRDisplaySubsystem](XR.XRDisplaySubsystem.html)> displays = new List<[XRDisplaySubsystem](XR.XRDisplaySubsystem.html)>();
            SubsystemManager.GetInstances(displays);
            if (displays.Count == 0)
            {
                [Debug.Log](Debug.Log.html)("No display subsystem found.");
                return null;
            }
            return displays[0];
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

