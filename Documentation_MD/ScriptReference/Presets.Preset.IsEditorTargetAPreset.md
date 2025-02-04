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

#  [Preset](Presets.Preset.html).IsEditorTargetAPreset

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

public static bool IsEditorTargetAPreset([Object](Object.html) target);

### Description

Returns true if the given target is a temporary UnityEngine.Object instance
created from inside a PresetEditor.

This method has to be used from inside a CustomEditor in order to change what
values are being displayed in the context of a Preset. Some CustomEditors,
like the ones for global settings, are being mixed with serialized values that
can be part of a Preset and global values shared between projects that are not
serializable. In a Preset inspector, those global values should be hidden or
at least disabled because changing them in the Preset would in fact change
them globally.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Presets;
    using UnityEditor.UIElements;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    [[CustomEditor](CustomEditor.html)(typeof(SomeSettings))]
    class SomeSettingsEditor : [Editor](Editor.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreateInspectorGUI()
        {
            var root = new [VisualElement](UIElements.VisualElement.html)();  
      
            // create UI for serialized data
            var aFloat = new [PropertyField](UIElements.PropertyField.html)(serializedObject.FindProperty("m_AFloat"));
            root.Add(aFloat);  
      
            // We are adding another field with an EditorPref data that we want to be excluded from the [Preset](Presets.Preset.html) UI.
            if (![Preset.IsEditorTargetAPreset](Presets.Preset.IsEditorTargetAPreset.html)(target))
            {
                var global = new [FloatField](UIElements.FloatField.html)("Global Pref");
                global.value = [EditorPrefs.GetFloat](EditorPrefs.GetFloat.html)("SomeGlobalSetting", 0.0f);
                global.RegisterCallback<ChangeEvent<float>>(evt => [EditorPrefs.SetFloat](EditorPrefs.SetFloat.html)("SomeGlobalSetting", evt.newValue));
                root.Add(global);
            }  
      
            return root;
        }
    }  
      
    class SomeSettings : [ScriptableObject](ScriptableObject.html)
    {
        public float m_AFloat;
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

