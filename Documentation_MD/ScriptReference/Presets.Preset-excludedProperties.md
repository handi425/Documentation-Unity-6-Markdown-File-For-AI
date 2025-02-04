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

#  [Preset](Presets.Preset.html).excludedProperties

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

public string[] excludedProperties;

### Description

List of properties to ignore when applying the Preset to an object.

Sets the list of properties or parent properties to ignore when applying the
Preset to an object.

    
    
    using UnityEngine;
    using UnityEditor.Presets;  
      
    static class PresetsExample
    {
        public static bool ApplyToWithExclusion([Preset](Presets.Preset.html) preset, [Transform](Transform.html) target, string[] exclusion)
        {
            var current = preset.excludedProperties;
            preset.excludedProperties = exclusion;
            var success = preset.ApplyTo(target);
            preset.excludedProperties = current;
            return success;
        }  
      
        public static void ApplyTransformPresetWithoutPosition([Preset](Presets.Preset.html) preset, [Transform](Transform.html) target)
        {
            if (ApplyToWithExclusion(preset, target, new[] { "m_LocalPosition" }))
            {
                [Debug.Log](Debug.Log.html)("The [Preset](Presets.Preset.html) has been applied and the position hasn't changed");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("The [Preset](Presets.Preset.html) was not applied");
            }
        }
    }
    
    
    
    using UnityEngine;
    using UnityEditor.Presets;  
      
    static class PresetsExample
    {
        public static bool ApplyOnlyTheYPosition([Preset](Presets.Preset.html) preset, [Transform](Transform.html) target)
        {
            var current = preset.excludedProperties;
            preset.excludedProperties = new[] { "m_LocalPosition.x", "m_LocalPosition.z" };
            var success = preset.ApplyTo(target, new[] { "m_LocalPosition" });
            preset.excludedProperties = current;
            return success;
        }
    }
    

Note: If every properties get ignored on a Preset, ApplyTo will always return
false. This is also the case when using ApplyTo(Object, string[]) and the
specified list of properties to apply are all ignored.

    
    
    using UnityEngine;
    using UnityEditor.Presets;  
      
    static class PresetsExample
    {
        public static bool ApplyAlwaysReturnFalse([Preset](Presets.Preset.html) preset, [Transform](Transform.html) target)
        {
            var current = preset.excludedProperties;
            preset.excludedProperties = new[] { "m_LocalPosition" };
            var success = preset.ApplyTo(target, new[] { "m_LocalPosition" });  // always false because we try to apply only the ignored property.
            preset.excludedProperties = current;
            return success;
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

