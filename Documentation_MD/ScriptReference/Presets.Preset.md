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

# Preset

class in UnityEditor.Presets

/

Inherits from:[Object](Object.html)

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

A Preset contains default values for an Object.

The Preset class contains the type of the Object used to create it and a list
of each serialized property/value pair of this Object. It can be used to store
informations from any serializable Object in the Editor and apply them back to
this Object or any other Object of the same type. Presets can also be saved as
Assets using the .preset extension in order to.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Presets;
    using UnityEngine;  
      
    public static class PresetUsageExample
    {
        // This method uses a [Preset](Presets.Preset.html) to copy the serialized values from the source to the target and return true if the copy succeed.
        public static bool CopyObjectSerialization(Object source, Object target)
        {
            [Preset](Presets.Preset.html) preset = new [Preset](Presets.Preset.html)(source);
            return preset.ApplyTo(target);
        }  
      
        // This method creates a [Preset](Presets.Preset.html) from a given Object and save it as an asset in the project.
        public static void CreatePresetAsset(Object source, string name)
        {
            [Preset](Presets.Preset.html) preset = new [Preset](Presets.Preset.html)(source);
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(preset, "Assets/" + name + ".preset");
        }
    }
    

### Properties

[excludedProperties](Presets.Preset-excludedProperties.html)| List of
properties to ignore when applying the Preset to an object.  
---|---  
[PropertyModifications](Presets.Preset.PropertyModifications.html)| Returns a
copy of the PropertyModification array owned by this Preset.  
  
### Constructors

[Preset](Presets.Preset-ctor.html)| Constructs a new Preset from a given
Object.  
---|---  
  
### Public Methods

[ApplyTo](Presets.Preset.ApplyTo.html)| Applies this Preset to the target
object.  
---|---  
[CanBeAppliedTo](Presets.Preset.CanBeAppliedTo.html)| Returns true if this
Preset can be applied to the target Object.  
[DataEquals](Presets.Preset.DataEquals.html)| Determines if the target object
has the same serialized values as the Preset.  
[GetPresetType](Presets.Preset.GetPresetType.html)| Returns the PresetType of
this Preset.  
[GetTargetFullTypeName](Presets.Preset.GetTargetFullTypeName.html)| Returns a
human readable string of this Preset's target fulltype, including namespace.  
[GetTargetTypeName](Presets.Preset.GetTargetTypeName.html)| Returns a human
readable string of this Preset's target type.  
[IsValid](Presets.Preset.IsValid.html)| Returns true if the Preset type of
this Preset is valid.  
[UpdateProperties](Presets.Preset.UpdateProperties.html)| Updates this
Preset's properties from the given Object's values. The given Object's type
must match this Preset's type.  
  
### Static Methods

[GetAllDefaultTypes](Presets.Preset.GetAllDefaultTypes.html)| Returns all the
PresetType that have at least one DefaultPreset entry in the default Presets
list.  
---|---  
[GetDefaultPresetsForObject](Presets.Preset.GetDefaultPresetsForObject.html)|
Gets the ordered list of Presets that set its default values when applied to
the target.  
[GetDefaultPresetsForType](Presets.Preset.GetDefaultPresetsForType.html)| Gets
an ordered list of DefaultPreset based on the specified PresetType.  
[IsEditorTargetAPreset](Presets.Preset.IsEditorTargetAPreset.html)| Returns
true if the given target is a temporary UnityEngine.Object instance created
from inside a PresetEditor.  
[RemoveFromDefault](Presets.Preset.RemoveFromDefault.html)| Remove the Preset
type from having default values in the project.  
[SetDefaultPresetsForType](Presets.Preset.SetDefaultPresetsForType.html)| Sets
a default list of Presets with a filter for a specific PresetType.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

