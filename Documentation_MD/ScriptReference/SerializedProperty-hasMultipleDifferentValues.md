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

#  [SerializedProperty](SerializedProperty.html).hasMultipleDifferentValues

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

public bool hasMultipleDifferentValues;

### Description

Does this property represent multiple different values due to multi-object
editing? (Read Only)

Returns true when there are multiple target objects, and they do not all have
the same value. Additional resources:
[SerializedObject.targetObjects](SerializedObject-targetObjects.html),
[SerializedObject.SetIsDifferentCacheDirty](SerializedObject.SetIsDifferentCacheDirty.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyHasMultipleDifferentValuesExample : [ScriptableObject](ScriptableObject.html)
    {
        public int m_Matching;
        public int m_Different;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) hasMultipleDifferentValues Example")]
        static void HasMultipleDifferentValuesExample()
        {
            var instance1 = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyHasMultipleDifferentValuesExample>();
            instance1.m_Matching = 1;
            instance1.m_Different = 1;  
      
            var instance2 = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyHasMultipleDifferentValuesExample>();
            instance2.m_Matching = 1;
            instance2.m_Different = 2;  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(new [ScriptableObject](ScriptableObject.html)[] { instance1, instance2 }))
            {
                var matchingProperty = serializedObject.FindProperty("m_Matching");
                var differentProperty = serializedObject.FindProperty("m_Different");  
      
                // Outputs
                //m_Matching  value: 1, matching: True
                //m_Different value: 1, matching: False
                [Debug.Log](Debug.Log.html)($"m_Matching  value: {matchingProperty.intValue}, matching: {!matchingProperty.hasMultipleDifferentValues}\n" +
                    $"m_Different value: {differentProperty.intValue}, matching: {!differentProperty.hasMultipleDifferentValues}");
            }
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

