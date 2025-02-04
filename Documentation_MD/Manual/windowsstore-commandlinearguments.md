[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-commandlinearguments.html)
  * [中文](/cn/current/Manual/windowsstore-commandlinearguments.html)
  * [日本語](/ja/current/Manual/windowsstore-commandlinearguments.html)
  * [한국어](/kr/current/Manual/windowsstore-commandlinearguments.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-commandlinearguments.html)
  * [中文](/cn/current/Manual/windowsstore-commandlinearguments.html)
  * [日本語](/ja/current/Manual/windowsstore-commandlinearguments.html)
  * [한국어](/kr/current/Manual/windowsstore-commandlinearguments.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * Command line arguments for UWP

[](windowsstore-appcallbacks.html)

AppCallbacks class reference

[](windowsstore-assocation-launching.html)

Association launching for UWP

# Command line arguments for UWP

You can launch Unity Players from the command line and pass in arguments to
change how the Player executes. Universal Windows Platform (UWP) apps don’t
accept command line arguments by default, so you have to pass them to an
AppCallbacks constructor in `App.xaml.cpp` or `App.cpp` to specify them.

This code example demonstrates how to do this:

    
    
    m_AppCallbacks = 
        ref new AppCallbacks
        (
            ref new Platform::Array<Platform::String\^> 
            {
                L"-force-gfx-direct" 
            }
        );
    

For more information on command line arguments for UWP, refer to [Unity
Standalone Player command line arguments](PlayerCommandLineArguments.html).

[](windowsstore-appcallbacks.html)

AppCallbacks class reference

[](windowsstore-assocation-launching.html)

Association launching for UWP

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

