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

# AudioClip

class in UnityEngine

/

Inherits from:[Audio.AudioResource](Audio.AudioResource.html)

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

[Switch to Manual](../Manual/class-AudioClip.html "Go to AudioClip Component
in the Manual")

### Description

A container for audio data.

An AudioClip stores the audio file either compressed as ogg vorbis or
uncompressed. AudioClips are referenced and used by AudioSources to play
sounds.  
  
Additional resources: [AudioClip component](../Manual/class-AudioClip.html) in
the Components Reference.

### Properties

[ambisonic](AudioClip-ambisonic.html)| Returns true if this audio clip is
ambisonic (read-only).  
---|---  
[channels](AudioClip-channels.html)| The number of channels in the audio clip.
(Read Only)  
[frequency](AudioClip-frequency.html)| The sample frequency of the clip in
Hertz. (Read Only)  
[length](AudioClip-length.html)| The length of the audio clip in seconds.
(Read Only)  
[loadInBackground](AudioClip-loadInBackground.html)| Corresponding to the
"Load In Background" flag in the inspector, when this flag is set, the loading
will happen delayed without blocking the main thread.  
[loadState](AudioClip-loadState.html)| Returns the current load state of the
audio data associated with an AudioClip.  
[loadType](AudioClip-loadType.html)| The load type of the clip (read-only).  
[preloadAudioData](AudioClip-preloadAudioData.html)| Preloads audio data of
the clip when the clip asset is loaded. When this flag is off, scripts have to
call AudioClip.LoadAudioData() to load the data before the clip can be played.
Properties like length, channels and format are available before the audio
data has been loaded.  
[samples](AudioClip-samples.html)| The length of the audio clip in samples.
(Read Only)  
  
### Public Methods

[GetData](AudioClip.GetData.html)| Fills an array with sample data from the
clip.  
---|---  
[LoadAudioData](AudioClip.LoadAudioData.html)| Loads the audio data of a clip.
Clips that have "Preload Audio Data" set will load the audio data
automatically.  
[SetData](AudioClip.SetData.html)| Set sample data in a clip.  
[UnloadAudioData](AudioClip.UnloadAudioData.html)| Unloads the audio data
associated with the clip. This works only for AudioClips that are based on
actual sound file assets.  
  
### Static Methods

[Create](AudioClip.Create.html)| Creates a user AudioClip with a name and with
the given length in samples, channels and frequency.  
---|---  
  
### Delegates

[PCMReaderCallback](AudioClip.PCMReaderCallback.html)| Delegate called each
time AudioClip reads data.  
---|---  
[PCMSetPositionCallback](AudioClip.PCMSetPositionCallback.html)| Delegate
called each time AudioClip changes read position.  
  
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

