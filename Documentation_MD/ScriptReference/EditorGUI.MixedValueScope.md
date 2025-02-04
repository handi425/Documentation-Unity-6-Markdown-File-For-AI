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

# MixedValueScope

struct in UnityEditor

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

Creates a group of controls that can visually represent a mixed value.

To configure a group of controls that can show a dash (-) if selected objects
have different values, add `EditorGUI.MixedValueScope` before the group and
set `newMixedValue` to true.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    [[CustomEditor](CustomEditor.html)(typeof(MixedValueComponentTest))]
    public class MixedValueComponentTestEditor : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            [SerializedProperty](SerializedProperty.html) serializedPropertyMyInt = serializedObject.FindProperty("MyInt");
            using (new [EditorGUI.MixedValueScope](EditorGUI.MixedValueScope.html)(serializedPropertyMyInt.hasMultipleDifferentValues))
            {
                [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
                int newValue = [EditorGUILayout.IntField](EditorGUILayout.IntField.html)("My Int", serializedPropertyMyInt.intValue);
                if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                    serializedPropertyMyInt.intValue = newValue;
            }
            serializedObject.ApplyModifiedProperties();
        }
    }  
      
    public class MixedValueComponentTest : [MonoBehaviour](MonoBehaviour.html)
    {
        public int MyInt;
    }
    

Additional resources: [EditorGUI.showMixedValue](EditorGUI-
showMixedValue.html).

### Constructors

[EditorGUI.MixedValueScope](EditorGUI.MixedValueScope-ctor.html)| Creates a
new MixedValueScope that determines the start of the group of mixed value
controls.  
---|---  
  
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

