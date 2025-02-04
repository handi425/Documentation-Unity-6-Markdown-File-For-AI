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

# AudioReverbFilter

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.AudioModule](UnityEngine.AudioModule.html)

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

[Switch to Manual](../Manual/class-AudioReverbFilter.html "Go to
AudioReverbFilter Component in the Manual")

### Description

The Audio Reverb Filter takes an Audio Clip and distorts it to create a custom
reverb effect.

Additional resources: [Audio Reverb Filter](../Manual/class-
AudioReverbFilter.html) information.

### Properties

[decayHFRatio](AudioReverbFilter-decayHFRatio.html)| Decay HF Ratio : High-
frequency to low-frequency decay time ratio. Ranges from 0.1 to 2.0. Default
is 0.5.  
---|---  
[decayTime](AudioReverbFilter-decayTime.html)| Reverberation decay time at
low-frequencies in seconds. Ranges from 0.1 to 20.0. Default is 1.0.  
[density](AudioReverbFilter-density.html)| Reverberation density (modal
density) in percent. Ranges from 0.0 to 100.0. Default is 100.0.  
[diffusion](AudioReverbFilter-diffusion.html)| Reverberation diffusion (echo
density) in percent. Ranges from 0.0 to 100.0. Default is 100.0.  
[dryLevel](AudioReverbFilter-dryLevel.html)| Mix level of dry signal in output
in millibels (mB). Ranges from -10000.0 to 0.0. Default is 0.  
[hfReference](AudioReverbFilter-hfReference.html)| Reference high frequency in
hertz (Hz). Ranges from 1000.0 to 20000.0. Default is 5000.0.  
[lfReference](AudioReverbFilter-lfReference.html)| Reference low-frequency in
hertz (Hz). Ranges from 20.0 to 1000.0. Default is 250.0.  
[reflectionsDelay](AudioReverbFilter-reflectionsDelay.html)| Late
reverberation level relative to room effect in millibels (mB). Ranges from
-10000.0 to 2000.0. Default is 0.0.  
[reflectionsLevel](AudioReverbFilter-reflectionsLevel.html)| Early reflections
level relative to room effect in millibels (mB). Ranges from -10000.0 to
1000.0. Default is -10000.0.  
[reverbDelay](AudioReverbFilter-reverbDelay.html)| Late reverberation delay
time relative to first reflection in seconds. Ranges from 0.0 to 0.1. Default
is 0.04.  
[reverbLevel](AudioReverbFilter-reverbLevel.html)| Late reverberation level
relative to room effect in millibels (mB). Ranges from -10000.0 to 2000.0.
Default is 0.0.  
[reverbPreset](AudioReverbFilter-reverbPreset.html)| Set/Get reverb preset
properties.  
[room](AudioReverbFilter-room.html)| Room effect level at low frequencies in
millibels (mB). Ranges from -10000.0 to 0.0. Default is 0.0.  
[roomHF](AudioReverbFilter-roomHF.html)| Room effect high-frequency level re.
low frequency level in millibels (mB). Ranges from -10000.0 to 0.0. Default is
0.0.  
[roomLF](AudioReverbFilter-roomLF.html)| Room effect low-frequency level in
millibels (mB). Ranges from -10000.0 to 0.0. Default is 0.0.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
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

