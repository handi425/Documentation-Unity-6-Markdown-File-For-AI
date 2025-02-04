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

**Method group is Obsolete**  

# Subsystem

class in UnityEngine

/

Implemented
in:[UnityEngine.SubsystemsModule](UnityEngine.SubsystemsModule.html)

Leave feedback

  

Implements interfaces:[ISubsystem](ISubsystem.html)

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

**Obsolete** Use SubsystemWithProvider instead.

### Description

A Subsystem is initialized from a
[SubsystemDescriptorWithProvider](SubsystemsImplementation.SubsystemDescriptorWithProvider.html)
for a given Subsystem (Example, Input, Display, etc.) and provides an
interface to interact with that given Subsystem until it is Destroyed. After a
Subsystem is created it can be Started or Stopped to turn on and off
functionality (and improve performance). The base type for subsystems only
exposes this functionality; this class is designed to be a base class for
derived classes that expose more functionality specific to a given Subsystem.  
  
Note: initializing a second Subsystem from the same SubsystemDescriptor will
return a reference to the existing Subsystem as only one Subsystem is
currently allowed for a single Subsystem provider.  
  
This subsystem base-class is deprecated. If you are creating a new subsystem
type, derive from
[SubsystemWithProvider](SubsystemsImplementation.SubsystemWithProvider.html)
instead.

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

