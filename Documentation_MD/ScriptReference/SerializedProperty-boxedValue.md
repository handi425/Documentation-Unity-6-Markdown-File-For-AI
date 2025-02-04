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

#  [SerializedProperty](SerializedProperty.html).boxedValue

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

public object boxedValue;

### Description

Value of the SerializedProperty, boxed as a System.Object.

This property represents the value of the SerializedProperty as a
System.Object which wraps the underlying type.  
  
This property makes it easier to write code that doesn't need the precise type
of a SerializedProperty to get or set its value. For example this property can
access any numeric type, strings, built-in types like [Vector3](Vector3.html)
and ManagedReference objects with the same syntax. This property can remove
the need for switch-case statements or slow alternatives based on .NET
Reflection to determine a SerializedProperty's type.  
  
Wrapping a value type as a heap-based System.Object requires a transformation
called "boxing", which adds a performance overhead. In cases where performance
is important and you know the type ahead of time, use the appropriate type-
specific accessors like [intValue](SerializedProperty-intValue.html),
[stringValue](SerializedProperty-stringValue.html), or
[managedReferenceValue](SerializedProperty-managedReferenceValue.html) instead
of this property. This removes the performance overhead that this property
requires for boxing.  
  
When your application sets this property, Unity attempts to unbox and convert
the provided System.Object into the property type of the SerializedProperty.
If this fails, Unity throws an InvalidCastException error.  
  
boxedValue has some limitations for properties of type
[SerializedPropertyType.Generic](SerializedPropertyType.Generic.html):

  * Structs and objects serialized by-value can be accessed, unless they contain fixed buffers.
  * The property cannot be an array or list. But accessing a property that is an element of an array or list is supported.
  * Unity built-in Struct types that are categorized in the Generic type cannot be accessed. But built-in types like [Vector3](Vector3.html) that have a their own entry in the [SerializedPropertyType](SerializedPropertyType.html) enum do work.

Additional resources: [propertyType](SerializedProperty-propertyType.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections.Generic;  
      
    // To try this example save it as a script called BoxedValueStructExample.cs,
    // then create an asset file from the Project Window context menu, then inspect it  
      
    [System.Serializable]
    public struct [Element](Unity.Android.Gradle.Element.html)
    {
        public int m_IntData;
        public [Color](Color.html) m_ColorData;
        public [Rect](Rect.html) m_Rect;  
      
        public void Change()
        {
            ++m_IntData;
            m_ColorData = new [Color](Color.html)([Random.Range](Random.Range.html)(0f, 1f), [Random.Range](Random.Range.html)(0f, 1f), [Random.Range](Random.Range.html)(0f, 1f), 1);
            m_Rect = new [Rect](Rect.html)([Random.Range](Random.Range.html)(0, 100), [Random.Range](Random.Range.html)(0, 100),
                [Random.Range](Random.Range.html)(0, 100), [Random.Range](Random.Range.html)(0, 100));
        }
    };  
      
    [CreateAssetMenu]
    public class BoxedValueStructExample : [ScriptableObject](ScriptableObject.html)
    {
        public [Element](Unity.Android.Gradle.Element.html) m_NewItem = new [Element](Unity.Android.Gradle.Element.html)();
        public List<[Element](Unity.Android.Gradle.Element.html)> m_ItemList = new List<[Element](Unity.Android.Gradle.Element.html)>();
    }  
      
    [[CustomEditor](CustomEditor.html)(typeof(BoxedValueStructExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class BoxedValueStructExampleEditor : [Editor](Editor.html)
    {
        [SerializedProperty](SerializedProperty.html) m_NewItemProp;
        [SerializedProperty](SerializedProperty.html) m_ListProp;  
      
        public void OnEnable()
        {
            m_NewItemProp = serializedObject.FindProperty("m_NewItem");
            m_ListProp = serializedObject.FindProperty("m_ItemList");
        }  
      
        public override void OnInspectorGUI()
        {
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_NewItemProp);  
      
            [GUILayout.Space](GUILayout.Space.html)(30);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Add New [Item](Progress.Item.html) to List"))
            {
                // Read full [Element](Unity.Android.Gradle.Element.html) struct
                [Element](Unity.Android.Gradle.Element.html) newItem = ([Element](Unity.Android.Gradle.Element.html))m_NewItemProp.boxedValue;  
      
                // Append a new item to list and set it to the same values as m_NewItem
                m_ListProp.arraySize++;
                m_ListProp.GetArrayElementAtIndex(m_ListProp.arraySize - 1).boxedValue = newItem;  
      
                // [Update](PlayerLoop.Update.html) NewItem to some new values
                newItem.Change();
                m_NewItemProp.boxedValue = newItem;  
      
                // Because boxedValue is used, the code above does not need to deal with fields inside the struct,
                // and it would not need to change as fields are added and removed to [Element](Unity.Android.Gradle.Element.html)
            }  
      
            [GUILayout.Space](GUILayout.Space.html)(30);
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_ListProp);  
      
            serializedObject.ApplyModifiedProperties();
        }
    }
    
    
    
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class BoxedValueExample
    {
        [[MenuItem](MenuItem.html)("Example/Log Property Values")]
        static void MenuCallback()
        {
            var log = new StringBuilder();
            var obj = [Selection.activeGameObject](Selection-activeGameObject.html);
            {
                log.AppendLine($"Contents of {obj.name}");
                LogProperties(obj, log);
            }  
      
            foreach (var comp in obj.GetComponents<[Component](Component.html)>())
            {
                log.AppendLine();
                log.AppendLine($"[Component](Component.html) {comp.GetType().ToString()}");
                LogProperties(comp, log);
            }  
      
            [Debug.Log](Debug.Log.html)(log.ToString());
        }  
      
        static void LogProperties(UnityEngine.Object obj, StringBuilder log)
        {
            using (var so = new [SerializedObject](SerializedObject.html)(obj))
            {
                var iterator = so.GetIterator();
                iterator.Next(true); // Move past root property  
      
                // Printing top level propertise only
                do
                {
                    log.Append(iterator.name);
                    log.Append(" type: ");
                    log.Append(iterator.propertyType);
                    LogValue(iterator, log);
                    log.AppendLine();
                }
                while (iterator.Next(false));
            }
        }  
      
        static void LogValue([SerializedProperty](SerializedProperty.html) serializedProperty, StringBuilder log)
        {
            // Don't attempt to print these types as strings
            if (serializedProperty.propertyType == [SerializedPropertyType.Generic](SerializedPropertyType.Generic.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.ObjectReference](SerializedPropertyType.ObjectReference.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html))
            {
                return;
            }  
      
            log.Append($" value: {serializedProperty.boxedValue}");
        }  
      
        [[MenuItem](MenuItem.html)("Example/Log Property Values", true)]
        static bool MenuValidation()
        {
            return [Selection.activeGameObject](Selection-activeGameObject.html) != null;
        }
    }
    

This is a recursive version of the example, with more information and
formatting, but still relying on boxedValue.

    
    
    using System.Collections.Generic;
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class RecursivePropertyLogExample
    {
        [[MenuItem](MenuItem.html)("Example/Log Property Values (Recursive)")]
        static void MenuCallback()
        {
            var obj = [Selection.activeGameObject](Selection-activeGameObject.html);
            {
                var log = new StringBuilder();
                log.AppendLine($"Contents of {obj.name}");
                LogProperties(obj, log);  
      
                // Log separately to avoid reaching the individual message size limit
                [Debug.Log](Debug.Log.html)(log.ToString());
            }  
      
            foreach (var comp in obj.GetComponents<[Component](Component.html)>())
            {
                var log = new StringBuilder();
                log.AppendLine($"[Component](Component.html) {comp.GetType().ToString()} of {obj.name}");
                LogProperties(comp, log);
                [Debug.Log](Debug.Log.html)(log.ToString());
            }
        }  
      
        static void LogProperties(UnityEngine.Object obj, StringBuilder log)
        {
            using (var so = new [SerializedObject](SerializedObject.html)(obj))
            {
                var iterator = so.GetIterator();
                iterator.Next(true); // Move past root property  
      
                // Prevent endless loops if [SerializeReference](SerializeReference.html) instances form cyclical graphs
                var visitedManagedReferences = new HashSet<long>();  
      
                bool visitChild;
                do
                {
                    visitChild = false;  
      
                    if (iterator.propertyType == [SerializedPropertyType.Generic](SerializedPropertyType.Generic.html))
                    {
                        visitChild = true;
                    }
                    else if (iterator.propertyType == [SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html))
                    {
                        long refId = iterator.managedReferenceId;
                        if (visitedManagedReferences.Add(refId))
                            visitChild = true; // First time seeing node, so visit it
                    }  
      
                    for (int i = 0; i < iterator.depth; i++)
                        log.Append("  ");  
      
                    if (iterator.name == "data")
                    {
                        // If this is an array element then it is more informative to use the name exposed by
                        // propertyPath, e.g. "data[7]" instead of "data".
                        var stringPos = iterator.propertyPath.LastIndexOf('.');
                        if (stringPos > 0)
                            log.Append(iterator.propertyPath.Substring(stringPos + 1));
                        else
                            log.Append(iterator.name);
                    }
                    else
                        log.Append(iterator.name);  
      
                    [LogType](LogType.html)(iterator, log);
                    LogValue(iterator, log);
                    log.AppendLine();  
      
                    // Skip past the "Array" child inside each property of type array
                    if (iterator.isArray)
                        iterator.Next(true);
                }
                while (iterator.Next(visitChild));
            }
        }  
      
        static void [LogType](LogType.html)([SerializedProperty](SerializedProperty.html) serializedProperty, StringBuilder log)
        {
            log.Append(" type: ");
            if (serializedProperty.propertyType == [SerializedPropertyType.Integer](SerializedPropertyType.Integer.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.Float](SerializedPropertyType.Float.html))
                log.Append(serializedProperty.numericType);
            else if (serializedProperty.propertyType == [SerializedPropertyType.Generic](SerializedPropertyType.Generic.html) && serializedProperty.isArray)
                log.Append("Array");
            else
                log.Append(serializedProperty.propertyType);
        }  
      
        static void LogValue([SerializedProperty](SerializedProperty.html) serializedProperty, StringBuilder log)
        {
            // use boxedValue to get and print the value as a string
            // There are a few special cases to improve the quality of the output  
      
            if (serializedProperty.propertyType == [SerializedPropertyType.Generic](SerializedPropertyType.Generic.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.AnimationCurve](SerializedPropertyType.AnimationCurve.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.Gradient](SerializedPropertyType.Gradient.html) ||
                serializedProperty.propertyType == [SerializedPropertyType.LayerMask](SerializedPropertyType.LayerMask.html))
            {
                return;
            }  
      
            if (serializedProperty.propertyType == [SerializedPropertyType.ObjectReference](SerializedPropertyType.ObjectReference.html))
            {
                if (ReferenceEquals(serializedProperty.objectReferenceValue, null))
                    log.Append($" value: null");
                else
                    log.Append($" instanceID: {serializedProperty.objectReferenceValue.GetInstanceID()}");
            }
            else if (serializedProperty.propertyType == [SerializedPropertyType.ManagedReference](SerializedPropertyType.ManagedReference.html))
            {
                if (ReferenceEquals(serializedProperty.managedReferenceValue, null))
                    log.Append($" value: null");
                else
                    log.Append($" refId: {serializedProperty.managedReferenceId} ({serializedProperty.managedReferenceFullTypename})");
            }
            else
            {
                log.Append($" value: {serializedProperty.boxedValue.ToString()}");
            }
        }  
      
        [[MenuItem](MenuItem.html)("Example/Log Property Values (Recursive)", true)]
        static bool ValidateMenuItem()
        {
            return [Selection.activeGameObject](Selection-activeGameObject.html) != null;
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

