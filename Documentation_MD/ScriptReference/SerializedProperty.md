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

# SerializedProperty

class in UnityEditor

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

SerializedProperty and [SerializedObject](SerializedObject.html) are classes
for editing properties on objects in a completely generic way that
automatically handles undo, multi-object editing and Prefab overrides.

SerializedProperty is primarily used to read or change the value of a
property. It can also iterate through the properties of an object using
[Next](SerializedProperty.Next.html). Additional resources:
[SerializedObject](SerializedObject.html) class, [Editor](Editor.html) class.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyObject : [ScriptableObject](ScriptableObject.html)
    {
        public int myInt = 42;
    }  
      
    public class SerializedPropertyTest : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            MyObject obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyObject>();
            [SerializedObject](SerializedObject.html) serializedObject = new UnityEditor.SerializedObject(obj);  
      
            [SerializedProperty](SerializedProperty.html) serializedPropertyMyInt = serializedObject.FindProperty("myInt");  
      
            [Debug.Log](Debug.Log.html)("myInt " + serializedPropertyMyInt.intValue);
        }
    }
    

### Properties

[animationCurveValue](SerializedProperty-animationCurveValue.html)| Value of a
animation curve property.  
---|---  
[arrayElementType](SerializedProperty-arrayElementType.html)| Type name of the
element in an array property. (Read Only)  
[arraySize](SerializedProperty-arraySize.html)| The number of elements in the
array.  
[boolValue](SerializedProperty-boolValue.html)| Value of a boolean property.  
[boundsIntValue](SerializedProperty-boundsIntValue.html)| Value of bounds with
integer values property.  
[boundsValue](SerializedProperty-boundsValue.html)| Value of bounds property.  
[boxedValue](SerializedProperty-boxedValue.html)| Value of the
SerializedProperty, boxed as a System.Object.  
[colorValue](SerializedProperty-colorValue.html)| Value of a color property.  
[contentHash](SerializedProperty-contentHash.html)| Provides the hash value
for the property. (Read Only)  
[depth](SerializedProperty-depth.html)| Nesting depth of the property. (Read
Only)  
[displayName](SerializedProperty-displayName.html)| Nice display name of the
property. (Read Only)  
[doubleValue](SerializedProperty-doubleValue.html)| Value of a float property
as a double.  
[editable](SerializedProperty-editable.html)| Is this property editable? (Read
Only)  
[enumDisplayNames](SerializedProperty-enumDisplayNames.html)| Display-friendly
names of enumeration of an enum property.  
[enumNames](SerializedProperty-enumNames.html)| Names of enumeration of an
enum property.  
[enumValueFlag](SerializedProperty-enumValueFlag.html)| Int32 representation
of an enum property with Mixed Values.  
[enumValueIndex](SerializedProperty-enumValueIndex.html)| Enum index of an
enum property.  
[exposedReferenceValue](SerializedProperty-exposedReferenceValue.html)| A
reference to another Object in the Scene. This reference is resolved in the
context of the SerializedObject containing the SerializedProperty.  
[fixedBufferSize](SerializedProperty-fixedBufferSize.html)| The number of
elements in the fixed buffer. (Read Only)  
[floatValue](SerializedProperty-floatValue.html)| Value of a float property.  
[gradientValue](SerializedProperty-gradientValue.html)| Value of a gradient
property.  
[hasChildren](SerializedProperty-hasChildren.html)| Does it have child
properties? (Read Only)  
[hash128Value](SerializedProperty-hash128Value.html)| The value of a Hash128
property.  
[hasMultipleDifferentValues](SerializedProperty-
hasMultipleDifferentValues.html)| Does this property represent multiple
different values due to multi-object editing? (Read Only)  
[hasVisibleChildren](SerializedProperty-hasVisibleChildren.html)| Does it have
visible child properties? (Read Only)  
[intValue](SerializedProperty-intValue.html)| Value of an integer property.  
[isArray](SerializedProperty-isArray.html)| Is this property an array? (Read
Only)  
[isDefaultOverride](SerializedProperty-isDefaultOverride.html)| Allows you to
check whether his property is a default override.Certain properties on Prefab
instances are default overrides.See PrefabUtility.IsDefaultOverride for more
information.  
[isExpanded](SerializedProperty-isExpanded.html)| Is this property expanded in
the inspector?  
[isFixedBuffer](SerializedProperty-isFixedBuffer.html)| Is this property a
fixed buffer? (Read Only)  
[isInstantiatedPrefab](SerializedProperty-isInstantiatedPrefab.html)| Is
property part of a Prefab instance? (Read Only)  
[longValue](SerializedProperty-longValue.html)| Value of an integer property
as a long.  
[managedReferenceFieldTypename](SerializedProperty-
managedReferenceFieldTypename.html)| String corresponding to the value of the
managed reference field full type string.  
[managedReferenceFullTypename](SerializedProperty-
managedReferenceFullTypename.html)| String corresponding to the value of the
managed reference object (dynamic) full type string.  
[managedReferenceId](SerializedProperty-managedReferenceId.html)| Id
associated with a managed reference.  
[managedReferenceValue](SerializedProperty-managedReferenceValue.html)| The
object assigned to a field with SerializeReference attribute.  
[minArraySize](SerializedProperty-minArraySize.html)| The smallest number of
elements in the array across all target objects. (Read Only)  
[name](SerializedProperty-name.html)| Name of the property. (Read Only)  
[numericType](SerializedProperty-numericType.html)| Return the precise type
for Integer and Floating point properties. (Read Only)  
[objectReferenceValue](SerializedProperty-objectReferenceValue.html)| Value of
an object reference property.  
[prefabOverride](SerializedProperty-prefabOverride.html)| Allows you to check
whether a property's value is overriden (i.e. different to the Prefab it
belongs to).  
[propertyPath](SerializedProperty-propertyPath.html)| Full path of the
property. (Read Only)  
[propertyType](SerializedProperty-propertyType.html)| Type of this property
(Read Only).  
[quaternionValue](SerializedProperty-quaternionValue.html)| Value of a
quaternion property.  
[rectIntValue](SerializedProperty-rectIntValue.html)| Value of a rectangle
with integer values property.  
[rectValue](SerializedProperty-rectValue.html)| Value of a rectangle property.  
[serializedObject](SerializedProperty-serializedObject.html)|
SerializedObject this property belongs to (Read Only).  
[stringValue](SerializedProperty-stringValue.html)| Value of a string
property.  
[tooltip](SerializedProperty-tooltip.html)| Tooltip of the property. (Read
Only)  
[type](SerializedProperty-type.html)| Type name of the property. (Read Only)  
[uintValue](SerializedProperty-uintValue.html)| Value of an integer property
as an unsigned int.  
[ulongValue](SerializedProperty-ulongValue.html)| Value of an integer property
as an unsigned long.  
[vector2IntValue](SerializedProperty-vector2IntValue.html)| Value of a 2D
integer vector property.  
[vector2Value](SerializedProperty-vector2Value.html)| Value of a 2D vector
property.  
[vector3IntValue](SerializedProperty-vector3IntValue.html)| Value of a 3D
integer vector property.  
[vector3Value](SerializedProperty-vector3Value.html)| Value of a 3D vector
property.  
[vector4Value](SerializedProperty-vector4Value.html)| Value of a 4D vector
property.  
  
### Public Methods

[ClearArray](SerializedProperty.ClearArray.html)| Remove all elements from the
array.  
---|---  
[Copy](SerializedProperty.Copy.html)| Returns a copy of the SerializedProperty
iterator in its current state.  
[CountInProperty](SerializedProperty.CountInProperty.html)| Count visible
children of this property, including this property itself.  
[CountRemaining](SerializedProperty.CountRemaining.html)| Count remaining
visible properties.  
[DeleteArrayElementAtIndex](SerializedProperty.DeleteArrayElementAtIndex.html)|
Delete the element at the specified index in the array.  
[DeleteCommand](SerializedProperty.DeleteCommand.html)| Deletes the array
element referenced by the SerializedProperty.  
[DuplicateCommand](SerializedProperty.DuplicateCommand.html)| Duplicates the
array element referenced by the SerializedProperty.  
[FindPropertyRelative](SerializedProperty.FindPropertyRelative.html)|
Retrieves the SerializedProperty at a relative path to the current property.  
[GetArrayElementAtIndex](SerializedProperty.GetArrayElementAtIndex.html)|
Returns the element at the specified index in the array.  
[GetEndProperty](SerializedProperty.GetEndProperty.html)| Retrieves the
SerializedProperty that defines the end range of this property.  
[GetEnumerator](SerializedProperty.GetEnumerator.html)| Retrieves an iterator
for enumerating over the visible child properties of the current property. If
the property is an array it will enumerate over the array elements.  
[GetFixedBufferElementAtIndex](SerializedProperty.GetFixedBufferElementAtIndex.html)|
Returns the element at the specified index in the fixed buffer.  
[InsertArrayElementAtIndex](SerializedProperty.InsertArrayElementAtIndex.html)|
Insert an new element at the specified index in the array.  
[MoveArrayElement](SerializedProperty.MoveArrayElement.html)| Move an array
element from srcIndex to dstIndex.  
[Next](SerializedProperty.Next.html)| Move to next property.  
[NextVisible](SerializedProperty.NextVisible.html)| Move to next visible
property.  
[Reset](SerializedProperty.Reset.html)| Move to first property of the object.  
  
### Static Methods

[DataEquals](SerializedProperty.DataEquals.html)| Compares the data for two
SerializedProperties. This method ignores paths and SerializedObjects.  
---|---  
[EqualContents](SerializedProperty.EqualContents.html)| See if contained
serialized properties are equal.  
  
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

