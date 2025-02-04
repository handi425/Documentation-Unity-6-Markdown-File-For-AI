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

#  [SerializedProperty](SerializedProperty.html).managedReferenceId

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

public long managedReferenceId;

### Description

Id associated with a managed reference.

Available when [propertyType](SerializedProperty-propertyType.html) is
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html).
If the reference is null then the Id is SerializeUtility.RefIdNull.  
  
Additional resources: [SerializeReference](SerializeReference.html),
[managedReferenceValue](SerializedProperty-managedReferenceValue.html),
[ManagedReferenceUtility.GetManagedReferenceIdForObject](Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class SerializedPropertyManagedReferenceIdExample : [ScriptableObject](ScriptableObject.html)
    {
        [Serializable]
        public class [Item](Progress.Item.html)
        {
            public int m_data = 1;
        }  
      
        [[SerializeReference](SerializeReference.html)]
        public [Item](Progress.Item.html) m_Item;  
      
        [[SerializeReference](SerializeReference.html)]
        public [Item](Progress.Item.html) m_Item2;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) ManagedReferenceId Example")]
        static void TestMethod1()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceIdExample>();
            scriptableObject.m_Item = new [Item](Progress.Item.html)();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                var itemProperty = serializedObject.FindProperty("m_Item");
                var item2Property = serializedObject.FindProperty("m_Item2");  
      
                // Set m_Item2 to point to the same object as m_Item
                // Note: managedReferenceValue could also be used here, for the same result
                item2Property.managedReferenceId = itemProperty.managedReferenceId;  
      
                serializedObject.ApplyModifiedProperties();
            }  
      
            // Check the results back on the live object  
      
            //Will print "Value of m_Item2.m_data: 1"
            [Debug.Log](Debug.Log.html)("Value of m_Item2.m_data: " + scriptableObject.m_Item2.m_data);  
      
            // Prove that both fields point to the same object
            scriptableObject.m_Item.m_data = 2;  
      
            //Will print "Value of m_Item2.m_data: 2"
            [Debug.Log](Debug.Log.html)("Value of m_Item2.m_data: " + scriptableObject.m_Item2.m_data);
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

