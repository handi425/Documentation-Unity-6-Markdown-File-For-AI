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

# IntegratedSubsystem

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

### Description

An IntegratedSubsystem is initialized from an
[IntegratedSubsystemDescriptor](IntegratedSubsystemDescriptor.html) for a
given Subsystem (Example, Input, Environment, Display, etc.) and provides an
interface to interact with that given IntegratedSubsystem until it is
Destroyed. After an IntegratedSubsystem is created it can be Started or
Stopped to turn on and off functionality (and preserve performance). The base
type for IntegratedSubsystem only exposes this functionality; this class is
designed to be a base class for derived classes that expose more functionality
specific to a given IntegratedSubsystem.  
  
Note: initializing a second IntegratedSubsystem from the same
IntegratedSubsystemDescriptor will return a reference to the existing
IntegratedSubsystem as only one IntegratedSubsystem is currently allowed for a
single IntegratedSubsystem provider.

### Properties

[running](IntegratedSubsystem-running.html)| Whether or not the subsystem is
running.  
---|---  
  
### Public Methods

[Destroy](IntegratedSubsystem.Destroy.html)| Destroys this instance of a
subsystem.  
---|---  
[Start](IntegratedSubsystem.Start.html)| Starts an instance of a subsystem.  
[Stop](IntegratedSubsystem.Stop.html)| Stops an instance of a subsystem.  
  
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

