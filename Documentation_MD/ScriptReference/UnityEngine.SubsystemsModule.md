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

# UnityEngine.SubsystemsModule

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

The Subsystem module contains the definitions and runtime support for general
subsystems in Unity.

### Classes

[IntegratedSubsystem](IntegratedSubsystem.html)| An IntegratedSubsystem is
initialized from an IntegratedSubsystemDescriptor for a given Subsystem
(Example, Input, Environment, Display, etc.) and provides an interface to
interact with that given IntegratedSubsystem until it is Destroyed. After an
IntegratedSubsystem is created it can be Started or Stopped to turn on and off
functionality (and preserve performance). The base type for
IntegratedSubsystem only exposes this functionality; this class is designed to
be a base class for derived classes that expose more functionality specific to
a given IntegratedSubsystem. Note: initializing a second IntegratedSubsystem
from the same IntegratedSubsystemDescriptor will return a reference to the
existing IntegratedSubsystem as only one IntegratedSubsystem is currently
allowed for a single IntegratedSubsystem provider.  
---|---  
[IntegratedSubsystemDescriptor](IntegratedSubsystemDescriptor.html)|
Information about a subsystem that can be queried before creating a subsystem
instance.  
[SubsystemDescriptorStore](SubsystemsImplementation.SubsystemDescriptorStore.html)|
Registration entry point for subsystems to register their descriptor.  
[SubsystemDescriptorWithProvider](SubsystemsImplementation.SubsystemDescriptorWithProvider.html)|
Information about a SubsystemWithProvider that can be queried before creating
a subsystem instance.  
[SubsystemManager](SubsystemManager.html)| Gives access to subsystems which
provide additional functionality through plugins.  
[SubsystemProvider](SubsystemsImplementation.SubsystemProvider.html)| A
provider that supplies data to a subsystem, generally for platform-specific
implementations.  
[SubsystemWithProvider](SubsystemsImplementation.SubsystemWithProvider.html)|
A subsystem is initialized from a SubsystemDescriptorWithProvider for a given
subsystem (Session, Plane, Face, etc.) and provides an interface to interact
with that given subsystem until it is Destroyed. After a subsystem is created,
it can be Started or Stopped to turn on and off functionality and preserve
performance. The base type for the subsystem only exposes this functionality;
this class is designed to be a base class for derived classes that expose more
functionality specific to a given subsystem.*Note:* Initializing a second
subsystem from the same subsystem descriptor will return a reference to the
existing subsystem, because only one subsystem is currently allowed for a
single subsystem provider.  
  
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

