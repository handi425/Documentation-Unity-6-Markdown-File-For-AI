[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-handle-crashes.html)
  * [中文](/cn/current/Manual/android-handle-crashes.html)
  * [日本語](/ja/current/Manual/android-handle-crashes.html)
  * [한국어](/kr/current/Manual/android-handle-crashes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-handle-crashes.html)
  * [中文](/cn/current/Manual/android-handle-crashes.html)
  * [日本語](/ja/current/Manual/android-handle-crashes.html)
  * [한국어](/kr/current/Manual/android-handle-crashes.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * Handle Android crashes

[](android-RequestingPermissions.html)

Request runtime permissions

[](android-quit.html)

Quit a Unity Android application

# Handle Android crashes

Crash handling for Unity applications on Android works as a chain of crash
handlers. The crash handler at the start of the chain receives the crash first
and it can process the crash and also forward the crash to the next crash
handler in the chain. The order of the crash handlers in the chain is defined
by the order in which they’re installed. The crash handler installed first is
the last one to receive the crash and the crash handler installed last is the
first one to receive the crash. By default, Unity acts as the first crash
handler in the chain. It processes crashes and forwards them to the next crash
handler in the chain, which is the Android system crash handler by default.

You can configure Unity to react differently to crashes and also add your own
custom crash handler to the chain. This page explains how to specify the
method Unity uses to handle crashes and how to create a custom crash handler.

## Specify how Unity handles crashes

If you don’t want to use Unity’s default crash handling behavior, you can use
the `-androidChainedSignalHandlerBehavior` command-line argument to change how
Unity reacts to crashes. This argument takes one of the following values:

**Behavior value** | **Description**  
---|---  
`legacy` | When a native crash occurs, Unity wraps and throws the crash as a java exception. Unity doesn’t forward the crash to the any installed crash handlers or to the default system.  
`disabled` | When a native crash occurs, Unity ignores it and Android forwards the crash directly to the next crash handler in the chain. This is either a custom crash handler, if one is installed, or the default system if not.  
**Note** : If you use this value, Unity services such as Unity Cloud
Diagnostics no longer handle crashes and won’t report them.  
  
For information on how to pass this command-line argument to Unity, see
[Specify Unity start-up arguments](android-custom-activity-command-line.html).

## Create and setup a custom crash handler

This section contains an example of how to create and set up your own crash
handler. For this to work, you must not use Unity’s legacy crash handling
behavior. For more information, refer to Specify how Unity handles crashes.

### Create a crash handler

The following code sample shows a custom crash handler. If you use the
[IL2CPP](./scripting-backends-il2cpp.html)A Unity-developed scripting back-end
which you can use as an alternative to Mono when building projects for some
platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) [scripting backend](scripting-
backends.html)A framework that powers scripting in Unity. Unity supports three
different scripting backends depending on target platform: Mono, .NET and
IL2CPP. Universal Windows Platform, however, supports only two: .NET and
IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend), you can place this example
`cpp` file directly into your Unity project. Unity then compiles it as part of
`libil2cpp.cpp`. If you use the [Mono](./scripting-backends-mono.html)A
scripting backend used in Unity. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#Mono) scripting backend, you must compile and
link your own shared library. For more information, refer to [Create a native
plug-in for Android](android-native-plugins-create.html).

**android_crash_handler.cpp**

    
    
    #include <android/log.h>
    #include <jni.h>
    #include <signal.h>
    
    struct sigaction s_PreviousHandler;
    bool s_SignalHandlerInstalled;
    
    static void MyCustomHandler(int sig, siginfo_t* info, void* ucontext)
    {
      __android_log_print(ANDROID_LOG_VERBOSE, "CustomCrashHandler", "Handling signal %d", sig);
      s_PreviousHandler.sa_sigaction(sig, info, ucontext);
    }
    
    extern "C" void InstallCustomSignalHandlers()
    {
      struct sigaction Action = {};
      Action.sa_sigaction = MyCustomHandler;
      // Note: Register more signals if you want.
      Action.sa_flags = SIGSEGV;
      sigaction(SIGSEGV, &Action, &s_PreviousHandler);
      s_SignalHandlerInstalled = true;
    }
    
    extern "C" JNIEXPORT void Java_com_unity3d_player_UnityPlayerActivity_InstallCustomSignalHandlersFromJava()
    {
      InstallCustomSignalHandlers();
    }
    
    extern "C" void UninstallCustomSignalHandlers()
    {
      if (s_SignalHandlerInstalled)
      {
          sigaction(SIGSEGV, &s_PreviousHandler, nullptr);
          s_SignalHandlerInstalled = false;
      }
    }
    

### Install the crash handler

To install the crash handler and have Unity use it to handle crashes, call the
`InstallCustomSignalHandlers` method in the above `cpp` file. You can do this
either through [C#](android-native-plugins-call.html) or Java code, however
it’s best practice to call this method from Java, because a crash can occur
after the Unity Player initializes, but before your C# code runs.

The following code sample shows how to call the `InstallCustomSignalHandlers`
method from Java code. To add it to your project, you can either install the
Java file as a **plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) (refer to [Create a Java or Kotlin
source plug-in](AndroidJavaSourcePlugins.html#CreateSourcePlugins)) or you can
modify an existing Java file in an [exported project](android-export-
process.html).

**Note** : Depending on where you call this method, it changes the behavior of
crash handling. If you call it before Unity runtime initialization, which is a
line of code that contains `mUnityPlayer = new UnityPlayer(this, this);`, then
during the native crash Unity’s crash handler is executed first and then your
signal handler is executed (if Unity forwards the signal). If you call
`InstallCustomSignalHandlers` after Unity runtime initialization, then during
the native crash your handler is executed first and it’s your responsibility
to forward the signal.

**UnityPlayerActivity.java**

    
    
    ...
      public native void InstallCustomSignalHandlersFromJava();
      static
      {
          System.loadLibrary("il2cpp");
      }
      // Setup activity layout
      @Override protected void onCreate(Bundle savedInstanceState)
      {
          InstallCustomSignalHandlersFromJava();
          ...
          mUnityPlayer = new UnityPlayer(this, this);
          setContentView(mUnityPlayer);
          mUnityPlayer.requestFocus();
      }
    ...
    

[](android-RequestingPermissions.html)

Request runtime permissions

[](android-quit.html)

Quit a Unity Android application

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

