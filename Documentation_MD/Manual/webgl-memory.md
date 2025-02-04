[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-memory.html)
  * [中文](/cn/current/Manual/webgl-memory.html)
  * [日本語](/ja/current/Manual/webgl-memory.html)
  * [한국어](/kr/current/Manual/webgl-memory.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-memory.html)
  * [中文](/cn/current/Manual/webgl-memory.html)
  * [日本語](/ja/current/Manual/webgl-memory.html)
  * [한국어](/kr/current/Manual/webgl-memory.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Memory in Unity Web

[](webgl-native-plugins-with-emscripten.html)

Web native plug-ins for Emscripten

[](webgl-caching.html)

Cache behavior in Web

# Memory in Unity Web

Memory constraints in Unity Web can restrict the complexity of the content you
run.

Web content runs in the browser. The browser allocates the memory in its
memory space that your application needs to run your content. The amount of
available memory varies depending on:

  * The device you use
  * The operating system you use
  * The browser you use, and whether it runs on a 32 or 64 processor
  * How much memory the browser’s JavaScript engine requires to parse your code
  * Whether the browser uses separate processes for each tab, or your content needs to share a memory space with all other open tabs.

**Note:** For information on security risks related to Web memory, refer to
[Security and Memory Resources](https://www.w3.org/TR/webgpu/#security-memory-
resources).

## Memory usage in Unity Web

The following areas of Unity Web content require the browser to allocate
significant amounts of memory.

  * The Unity heap
  * Asset data
  * Garbage collection

## Unity heap

Unity uses a memory heap to store all Unity engine runtime objects. These
include managed and native objects, loaded Assets, **Scenes** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), and **shaders** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). This is like the memory that Unity
Players use on any other platform.

The Unity heap is a contiguous block of allocated memory. Unity supports
automatic resizing for the heap to suit the needs of the application. The heap
size expands as an application runs, and can expand up to 2GB. Unity creates
this memory heap as a [Memory object](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/Memory). The
Memory object’s buffer property is a re-sizable ArrayBuffer that holds the raw
bytes of memory accessed by WebAssembly code.

Automatic resizing of the heap can cause your application to crash if the
browser fails to allocate a contiguous memory block in the address space. For
this reason, it’s important to keep the Unity heap size as small as possible.
Therefore, be mindful when you are planning the memory usage of your
application. If you want to test the size of your Unity heap, you can use the
[Profiler](Profiler.html)A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) to profile the contents of the
memory block.

You can control the initial size and growth of the heap by using the **Memory
Growth Mode** options in the [Web Player Settings](class-
PlayerSettingsWebGL.html). The default options are configured to work well for
all desktop use cases. However, for mobile browsers you need to use the
advanced tuning options. For mobile browsers, it’s recommended to configure
the **Initial Memory Size** to the typical heap usage of the application.

## Asset data

When you create a Unity Web build, Unity generates a `.data` file. This
contains all the Scenes and Assets the application needs to launch. Because
Unity Web doesn’t have access to the real file system, it creates a virtual
memory file system, and the browser unpacks the `.data` file here. The
Emscripten framework (JavaScript) allocates this memory file system in the
browser memory space. While your content runs, the browser memory keeps the
uncompressed data. To keep both download times and memory usage low, try to
keep this uncompressed data as small as possible.

To reduce memory use, you can pack your Asset data into AssetBundles.
AssetBundles offer full control over your asset downloads. You can control
when your application downloads an asset, and when the runtime unloads it. You
can unload unused assets to free up memory.

`AssetBundles` are downloaded directly into the Unity heap, so these don’t
result in extra allocation by the browser.

Enable **Data Caching** to automatically cache the Asset data in your content
on the user’s machine. This means you don’t need to re-download that data
during later runs. The Unity Web loader implements Data Caching with the
IndexedDB API. This option lets you to cache files which are too large for the
browser to cache natively.

Data caching enables the browser to store application data on the user’s
machine. Browsers often limit the amount you can store in their cache and the
maximum file size that can be cached. This is often not enough for an
application to run smoothly. The Unity Web loader Caching with the `IndexedDB`
API that lets Unity store the data in the IndexedDB instead of the browser
cache.

To enable the Data Caching option go to **File** > **Build Settings** >
**Player Settings** > **Publishing Settings**.

## Garbage collection

Garbage collection is the process of locating and freeing up unused memory.
For an overview on how Unity garbage collection works, refer to [Automatic
Memory Management](performance-managed-memory.html). To debug the garbage
collection process, use the Unity [Profiler](Profiler.html).

Due to a security limitation of WebAssembly, user programs are not allowed to
examine the native execution stack to prevent possible exploits.

This means that on the Web platform, the GC can only run when no managed code
is executing (which could potentially reference live C# objects). This occurs
at the end of every rendered game frame.

In other words, on the Web platform, the garbage collector can’t run in the
middle of executing C# code, and only runs at the end of each program frame.
This discrepancy causes some differences in garbage collection behavior on Web
compared to other platforms.

Because of these differences, pay close attention to code that performs a lot
of temporary allocations per-frame, especially if these allocations might
exhibit a sequence of linear size growth. Such allocations may cause a
temporary quadratic memory growth pressure for the garbage collector.

As an example, if you have a long-running loop, the following code might fail
when you run it on Web because the garbage collector doesn’t run between
iterations of the for loop. In this case, the garbage collector can’t free up
memory that the intermediate string objects use and will run out of memory in
the Unity heap.

    
    
    string hugeString = "";
     
    for (int i = 0; i < 100000; i++)
    {
       hugeString += "foo";
    }
    

In the above example, the length of `hugeString` at the end of the loop is 3 *
100000 = 300000 characters. The code, however, generates a hundred thousand
temporary strings before producing the final string. The total allocated
memory throughout the loop is 3 * (1 + 2 + 3 + … + 100000) = 3 * (100000 *
100001 / 2) = 15 gigabytes.

On native platforms, the garbage collector continuously cleans up previous
temporary copies of the string while the loop executes. So the above code
doesn’t require 15 GB of RAM in total to run.

On the Web platform, the garbage collector doesn’t reclaim the temporary
string copies until the end of the frame. As a result, the above code runs out
of memory attempting to allocate 15 GB of RAM.

The following code shows a second example where this type of temporary
quadratic memory pressure can occur:

    
    
    byte[] data;
     
    for (int i = 0; i < 100000; i++)
    {
       data = new byte[i];
       // do something temporary with data[]
    } 
    

Here the code allocates 1 + 2 + 3 + … + 100000 bytes = 5 GB worth of bytes
temporarily, even though only the last 100 KB array is preserved. This causes
the program to seemingly run out of memory on the Web platform even though
only 100 KB are necessary in the final output.

To limit these types of issues, avoid code constructs that perform
quadratically increasing amounts of temporary memory allocations. Instead,
either pre-allocate the final needed data size, or use a `List<T>` or similar
data structure that performs geometrically increasing capacity reservations
that mitigate the temporary memory pressure.

For example, with the `List<T>` container, consider using the
`List<T>.ReserveCapacity()` function that enables pre-allocating the needed
capacity, if you know the final size of the data structure. Likewise, consider
using the `List<T>.TrimExcess()` function when shrinking the size of a
container that previously held several megabytes of memory.

**Note:** When you use C# delegates or events such as `Delegate`, `Action`,
`Func`, these classes internally utilize similar linear growth allocations as
above. Avoid excessive amounts of per-frame delegate registrations and
unregistrations with these classes to minimize the temporary memory pressure
for the garbage collector on the Web platform.

## Additional resources

  * [Automatic Memory Management](performance-managed-memory.html)
  * [Garbage Collector](performance-garbage-collector.html)

[](webgl-native-plugins-with-emscripten.html)

Web native plug-ins for Emscripten

[](webgl-caching.html)

Cache behavior in Web

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

