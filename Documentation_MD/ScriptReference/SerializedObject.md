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

# SerializedObject

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

SerializedObject and [SerializedProperty](SerializedProperty.html) are classes
for editing serialized fields on [Unity objects](Object.html) in a completely
generic way. These classes automatically handle dirtying individual serialized
fields so they will be processed by the [Undo](Undo.html) system and styled
correctly for Prefab overrides when drawn in the Inspector.

In many cases, you may create tools to modify objects in your project. For
instance, the following script example creates a menu item that resets the
local position of all GameObjects currently selected. Put it in a file called
Example1.cs in a folder called Editor:

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    static class Example1
    {
        [[MenuItem](MenuItem.html)("Edit/Reset Selected Objects [Position](UIElements.Position.html) (No [Undo](Undo.html))")]
        static void ResetPosition()
        {
            // this action will not be undoable
            foreach (var go in [Selection.gameObjects](Selection-gameObjects.html))
                go.transform.localPosition = [Vector3.zero](Vector3-zero.html);
        }
    }
    

Although you can edit objects via their API points in this way, you would also
have to use other editor APIs to specify which components have been dirtied so
that this action would be undoable and would be detected as a change the next
time the Scene is saved, and so on. In contrast, using SerializedObject
handles this process automatically. The following script example has the same
effect as the previous one, but is also undoable and is tracked as a change in
the Scene. Put it in a file called Example2.cs in a folder called Editor:

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    static class Example2
    {
        [[MenuItem](MenuItem.html)("Edit/Reset Selected Objects [Position](UIElements.Position.html)")]
        static void ResetPosition()
        {
            var transforms = Selection.gameObjects.Select(go => go.transform).ToArray();
            var so = new [SerializedObject](SerializedObject.html)(transforms);
            // you can Shift+Right Click on property names in the Inspector to see their paths
            so.FindProperty("m_LocalPosition").vector3Value = [Vector3.zero](Vector3-zero.html);
            so.ApplyModifiedProperties();
        }
    }
    

SerializedObject opens a data stream to one or more target [Unity
objects](Object.html) at a time, which allows you to simultaneously edit
serialized data that the objects share in common. For example, if you have
several [Behaviours](Behaviour.html) of different types in the data stream,
the only property they have in common may be 'm_Enabled'.  
  
When you first create a SerializedObject instance it is up-to-date. Any
changes that you make to a [SerializedProperty](SerializedProperty.html)
accessed within this data stream must ultimately be flushed via the
[SerializedObject.ApplyModifiedProperties](SerializedObject.ApplyModifiedProperties.html)
method. If you keep a reference to a SerializedObject instance for more than
one frame, you must make sure to manually call its
[SerializedObject.Update](SerializedObject.Update.html) method before you read
any data from it, as one or more target objects may have been modified
elsewhere, such as from a separate SerializedObject stream. Respectively, note
that two different SerializedObject streams with the same target objects are
independent from one another and you must manually synchronize them in this
fashion if one or more of them is maintained over the course of several
frames.  
  
One of the most common uses of the SerializedObject and
[SerializedProperty](SerializedProperty.html) classes is when creating custom
[Editors](Editor.html), where using SerializedObject is the recommended
approach as opposed to modifying inspected target objects directly.  
  
The following example script defines a component that animates an object’s
local position using a sine function. Put it in a script called
SineAnimation.cs:

    
    
    using UnityEngine;  
      
    public class SineAnimation : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) axis { get { return m_Axis; } set { m_Axis = value; } }
        [[SerializeField](SerializeField.html)]
        private [Vector3](Vector3.html) m_Axis = [Vector3.up](Vector3-up.html);  
      
        public float period { get { return m_Period; } set { m_Period = value; } }
        [[SerializeField](SerializeField.html)]
        private float m_Period = 1f / [Mathf.PI](Mathf.PI.html);  
      
        public float amplitude { get { return m_Amplitude; } set { m_Amplitude = value; } }
        [[SerializeField](SerializeField.html)]
        private float m_Amplitude = 1f;  
      
        public float phaseShift { get { return m_PhaseShift; } set { m_PhaseShift = [Mathf.Clamp01](Mathf.Clamp01.html)(value); } }
        [[SerializeField](SerializeField.html), Range(0f, 1f)]
        private float m_PhaseShift;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            transform.localPosition = m_Axis * m_Amplitude * [Mathf.Sin](Mathf.Sin.html)(([Time.time](Time-time.html) + m_PhaseShift) / m_Period);
        }  
      
        void OnValidate()
        {
            m_PhaseShift = [Mathf.Clamp01](Mathf.Clamp01.html)(m_PhaseShift);
        }
    }
    

The following example script defines a custom [Editor](Editor.html) for
SineAnimation that adds a button after the default controls to randomize the
sine function parameters. Put it in a file called SineAnimationEditor.cs in a
folder called Editor:

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(SineAnimation)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class SineAnimationEditor : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            base.OnInspectorGUI();
            if ([GUILayout.Button](GUILayout.Button.html)("Randomize Sine Function", [EditorStyles.miniButton](EditorStyles-miniButton.html)))
            {
                serializedObject.FindProperty("m_Period").floatValue = [Random.Range](Random.Range.html)(0f, 10f);
                serializedObject.FindProperty("m_Amplitude").floatValue = [Random.Range](Random.Range.html)(0f, 10f);
                serializedObject.FindProperty("m_PhaseShift").floatValue = [Random.Range](Random.Range.html)(0f, 1f);
                serializedObject.ApplyModifiedProperties();
            }
        }
    }
    

The [Editor](Editor.html) class has a [serializedObject](Editor-
serializedObject.html) property that provides a stream to all of the inspected
targets (SineAnimation components in this case), which makes it easy to
support editing multiple objects at the same time. Because this
SerializedObject instance persists for the lifetime of the
[Editor](Editor.html) instance, the base implementation of OnInspectorGUI
handles calling Update before drawing any controls, as well as calling
ApplyModifiedProperties after any user interaction. As such, modifications
made when pressing the button added to this inspector must all be flushed via
ApplyModifiedProperties before the method exits, or they will be lost the next
time the base implementation of
[Editor.OnInspectorGUI](Editor.OnInspectorGUI.html) calls the
[SerializedObject.Update](SerializedObject.Update.html) method on the
[serializedObject](Editor-serializedObject.html) instance.  
  
Note that flushing data to a Unity object via
[SerializedObject.ApplyModifiedProperties](SerializedObject.ApplyModifiedProperties.html)
will not respect any data validation logic you may have in property setters
associated with the serialized fields. In this example, the value of the
'm_PhaseShift' field is clamped between 0 and 1, both in the phaseShift
property setter and in the UI (via the RangeAttribute). Because users can
access 'm_PhaseShift' via [SerializedProperty](SerializedProperty.html) (as
well as by editing the asset on disk) and not only via the 'phaseShift' API or
the UI, it is necessary to also clamp it to the valid range in the
[MonoBehaviour.OnValidate](MonoBehaviour.OnValidate.html) callback, which will
sanitize the data when the [Unity object](Object.html) is loaded.  
  
Also note that although SerializedObject is designed to work with multiple
targets, the value getter properties on the SerializedProperty class (e.g.,
[floatValue](SerializedProperty-floatValue.html),
[vector3Value](SerializedProperty-vector3Value.html)) are not multi-select
friendly. As such, assigning a value to them will affect all targets, but
reading a value from them only returns the value associated with the first
target in the list.  
  
Additional resources: [SerializedProperty](SerializedProperty.html),
[SerializeField](SerializeField.html), [Editor](Editor.html),
[MonoBehaviour.OnValidate](MonoBehaviour.OnValidate.html),
[hasMultipleDifferentValues](SerializedProperty-
hasMultipleDifferentValues.html).

### Properties

[context](SerializedObject-context.html)| The context used to store and
resolve ExposedReference types. This is set by the SerializedObject
constructor.  
---|---  
[forceChildVisibility](SerializedObject-forceChildVisibility.html)| Controls
the visibility of the child hidden fields.  
[hasModifiedProperties](SerializedObject-hasModifiedProperties.html)| Is true
when the SerializedObject has a modified property that has not been applied.  
[isEditingMultipleObjects](SerializedObject-isEditingMultipleObjects.html)|
Does the serialized object represents multiple objects due to multi-object
editing? (Read Only)  
[maxArraySizeForMultiEditing](SerializedObject-
maxArraySizeForMultiEditing.html)| Defines the maximum size beyond which
arrays cannot be edited when multiple objects are selected.  
[targetObject](SerializedObject-targetObject.html)| The inspected object (Read
Only).  
[targetObjects](SerializedObject-targetObjects.html)| The inspected objects
(Read Only).  
  
### Constructors

[SerializedObject](SerializedObject-ctor.html)| Create SerializedObject for
inspected object.  
---|---  
  
### Public Methods

[ApplyModifiedProperties](SerializedObject.ApplyModifiedProperties.html)|
Apply property modifications.  
---|---  
[ApplyModifiedPropertiesWithoutUndo](SerializedObject.ApplyModifiedPropertiesWithoutUndo.html)|
Applies property modifications without registering an undo operation.  
[CopyFromSerializedProperty](SerializedObject.CopyFromSerializedProperty.html)|
Copies a value from a SerializedProperty to the corresponding serialized
property on the serialized object.  
[CopyFromSerializedPropertyIfDifferent](SerializedObject.CopyFromSerializedPropertyIfDifferent.html)|
Copies a changed value from a SerializedProperty to the corresponding
serialized property on the serialized object.  
[FindProperty](SerializedObject.FindProperty.html)| Find serialized property
by name.  
[GetIterator](SerializedObject.GetIterator.html)| Get the first serialized
property.  
[SetIsDifferentCacheDirty](SerializedObject.SetIsDifferentCacheDirty.html)|
Update hasMultipleDifferentValues cache on the next /Update()/ call.  
[Update](SerializedObject.Update.html)| Update serialized object's
representation.  
[UpdateIfRequiredOrScript](SerializedObject.UpdateIfRequiredOrScript.html)|
Update serialized object's representation, only if the object has been
modified since the last call to Update or if it is a script.  
  
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

