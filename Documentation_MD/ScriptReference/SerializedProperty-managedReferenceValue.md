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

#  [SerializedProperty](SerializedProperty.html).managedReferenceValue

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

public object managedReferenceValue;

### Description

The object assigned to a field with
[SerializeReference](SerializeReference.html) attribute.

For use when [propertyType](SerializedProperty-propertyType.html) is
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html).  
  
  
  
The value object must be a type that is compatible with the base type of the
managed reference field (that is, the managed reference field that the
serialized property is referencing).  
  
Additional resources: [SerializeReference](SerializeReference.html),
[propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using Object = UnityEngine.Object;  
      
    public class SerializedPropertyManagedReferenceValueExample : [ScriptableObject](ScriptableObject.html)
    {
        [Serializable]
        public class [Item](Progress.Item.html)
        {
            public int m_data = 1;  
      
            public int DoCalculation()
            {
                // Could be querying some external data, or other calculation that cannot be
                // made entirely based on the local object state
                m_data++;
                return m_data * 2;
            }
        }  
      
        [[SerializeReference](SerializeReference.html)]
        public [Item](Progress.Item.html) m_Item;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) ManagedReferenceValue Example1")]
        static void TestMethod1()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceValueExample>();
            var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject);  
      
            // Allocate and assign an object to the m_Item field via managedReferenceValue
            var referenceProperty = serializedObject.FindProperty("m_Item");
            referenceProperty.managedReferenceValue = new [Item](Progress.Item.html)();  
      
            // Change a value of the object's field
            referenceProperty.FindPropertyRelative("m_data").intValue = 99;  
      
            // Apply the change back to the "live" object
            serializedObject.ApplyModifiedProperties();  
      
            // Will print "Value of m_data: 99"
            [Debug.Log](Debug.Log.html)("Value of m_data: " + scriptableObject.m_Item.m_data);
        }  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) ManagedReferenceValue Example2")]
        static void TestMethod2()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceValueExample>();
            scriptableObject.m_Item = new [Item](Progress.Item.html)();  
      
            var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject);
            var referenceProperty = serializedObject.FindProperty("m_Item");  
      
            // The "live" referenced object can be accessed so we can call a method on it
            (referenceProperty.managedReferenceValue as [Item](Progress.Item.html)).DoCalculation();  
      
            // The serialized state inside the [SerializedObject](SerializedObject.html) is now out of data with the change
            // of m_data on the live object, but can be brought back in sync by calling [Update](PlayerLoop.Update.html)()
            var serializedDataValue = serializedObject.FindProperty("m_Item.m_data").intValue;
            serializedObject.Update();
            var updatedSerializedDataValue = serializedObject.FindProperty("m_Item.m_data").intValue;  
      
            // Will print: "Value of m_data before update: 1 and after update: 2"
            [Debug.Log](Debug.Log.html)("Value of m_data before update: " + serializedDataValue + " and after update: " + updatedSerializedDataValue);
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

