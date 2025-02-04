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

#  [SerializedProperty](SerializedProperty.html).gradientValue

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

public [Gradient](Gradient.html) gradientValue;

### Description

Value of a gradient property.

Additional resources: [propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.Gradient](SerializedPropertyType.Gradient.html),
[Gradient](Gradient.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [CreateAssetMenu]
    public class SerializedPropertyGradientExample : [ScriptableObject](ScriptableObject.html)
    {
        public [Gradient](Gradient.html) m_Gradient;  
      
        [Range(0, 1)]
        public float m_EvaluationTime;  
      
        public SerializedPropertyGradientExample()
        {
            // Establish a default gradient
            var colorKeys = new [GradientColorKey](GradientColorKey.html)[]
            {
                new [GradientColorKey](GradientColorKey.html)() { color = [Color.red](Color-red.html), time = 0.0f },
                new [GradientColorKey](GradientColorKey.html)() { color = [Color.green](Color-green.html), time = 0.5f },
                new [GradientColorKey](GradientColorKey.html)() { color = [Color.blue](Color-blue.html), time = 1.0f }
            };
            var alphaKeys = new [GradientAlphaKey](GradientAlphaKey.html)[]
            {
                new [GradientAlphaKey](GradientAlphaKey.html)() { alpha = 0.5f, time = 0.0f },
                new [GradientAlphaKey](GradientAlphaKey.html)() { alpha = 1.0f, time = 1.0f }
            };
            m_Gradient = new [Gradient](Gradient.html)();
            m_Gradient.SetKeys(colorKeys, alphaKeys);
        }
    }  
      
    // Override the default inspector behavior to add extra text line after the two properties
    [[CustomEditor](CustomEditor.html)(typeof(SerializedPropertyGradientExample))]
    public class SerializedPropertyGradientExampleEditor : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            DrawDefaultInspector();  
      
            var gradient = serializedObject.FindProperty("m_Gradient").gradientValue;
            var evalPoint = serializedObject.FindProperty("m_EvaluationTime").floatValue;
            [GUILayout.Label](GUILayout.Label.html)($"Gradiant at time {evalPoint}: {gradient.Evaluate(evalPoint)}");
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

