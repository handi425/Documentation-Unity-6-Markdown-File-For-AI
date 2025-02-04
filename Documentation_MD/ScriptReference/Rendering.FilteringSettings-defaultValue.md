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

#  [FilteringSettings](Rendering.FilteringSettings.html).defaultValue

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

public static [Rendering.FilteringSettings](Rendering.FilteringSettings.html)
defaultValue;

### Description

Creates a `FilteringSettings` struct that contains default values for all
properties. With these default values, Unity does not perform any filtering.

To override values at the time that you create the struct, use the
[FilteringSettings constructor](Rendering.FilteringSettings-ctor.html).  
  
This example demonstrates the syntax for creating a default
`FilteringSettings` struct with default values.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class FilteringSettingsExample
    {
        public [FilteringSettings](Rendering.FilteringSettings.html) CreateFilteringSettings()
        {
            // Instantiate a [FilteringSettings](Rendering.FilteringSettings.html) struct with the default value
            // (i.e., perform no filtering)
            [FilteringSettings](Rendering.FilteringSettings.html) defaultFilteringSettings = [FilteringSettings.defaultValue](Rendering.FilteringSettings-defaultValue.html);  
      
            return defaultFilteringSettings;
        }
    }
    

Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a
simple render loop in a custom render pipeline](../Manual/srp-creating-simple-
render-loop.html).

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

